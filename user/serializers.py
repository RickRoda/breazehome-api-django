from user.models import Profile, User, Question
from rest_auth.serializers import LoginSerializer
from user.models import Profile, User
from django.conf import settings
from rest_framework import serializers
from django.contrib.auth.forms import PasswordResetForm
from django.utils.translation import ugettext_lazy as _
from django.core.signing import Signer

try:
    from allauth.account import app_settings as allauth_settings
    from allauth.utils import (email_address_exists,
                               get_username_max_length)
    from allauth.account.adapter import get_adapter
    from allauth.account.utils import setup_user_email
except ImportError:
    raise ImportError("allauth needs to be added to INSTALLED_APPS.")


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(
        many=False,
        read_only=False,
        required=False
    )
    password = serializers.CharField(
        write_only=True
    )


    class Meta:
        model = User
        fields = ('id', 'url', 'password', 'username',  'email', 'is_superuser', 'phone_number', 'profile')
        write_only_fields = ('password',)

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})  
        user = super(UserSerializer, self).create(validated_data)  
        user.set_password(validated_data['password'])
        user.save()
        self.create_or_update_profile(user, profile_data)
        return user

    def update(self, instance, validated_data):  
        profile_data = validated_data.pop('profile', None)
        self.create_or_update_profile(instance, profile_data)
        return super(UserSerializer, self).update(instance, validated_data)

    def create_or_update_profile(self, user, profile_data):
        profile, created = Profile.objects.get_or_create(user=user, defaults=profile_data)
        if not created and profile_data is not None:
            super(UserSerializer, self).update(profile, profile_data)


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_settings.USERNAME_MIN_LENGTH,
        required=allauth_settings.USERNAME_REQUIRED
    )
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    
    question = serializers.IntegerField(required=True)
    answer = serializers.CharField(required=True)
    

    profile = ProfileSerializer(
        many=False,
        read_only=False,
        required=False
    )

    def validate_username(self, username):
        username = get_adapter().clean_username(username)
        return username

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])

        
        if (request.data['question'] != '0'):
            question = Question.objects.get(pk=request.data['question'])
            answer = ''.join(request.data['answer'].split()).lower()
            answerSignSliced = Signer().sign(answer).split(':', 1)[1]
        else:
            question = 0
            answerSignSliced = ''
        

        try:
            profile_data = request.data['profile']
            profile_data.question = question
            profile_data.answer = answer
        except KeyError:
            profile_data = { 'question' : question , 'answer' : answerSignSliced}
        self.create_or_update_profile(user, profile_data)
        return user

    def update(self, instance, validated_data):  
        profile_data = validated_data.pop('profile', None)
        self.create_or_update_profile(instance, profile_data)
        return super(RegisterSerializer, self).update(instance, validated_data)

    def create_or_update_profile(self, user, profile_data):
        profile, created = Profile.objects.get_or_create(user=user, defaults=profile_data)
        if not created and profile_data is not None:
            super(RegisterSerializer, self).update(profile, profile_data)

class PasswordResetSerializer(serializers.Serializer):

    """
    Serializer for requesting a password reset e-mail.
    """

    email = serializers.EmailField()

    password_reset_form_class = PasswordResetForm

    def validate_email(self, value):
        
        self.reset_form = self.password_reset_form_class(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(_('Error'))

        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError(_('Invalid e-mail address'))

        return value

    def save(self):
        request = self.context.get('request')
        
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
            'request': request,
        }
        self.reset_form.save(**opts)

class PasswordResetConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField(max_length=10, allow_blank=True)

class NewPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(max_length=64, allow_blank=True)
    new_password2 = serializers.CharField(max_length=64, allow_blank=True)

    def validate_password(new_password, new_password2):
        if new_password == new_password2:
            return True
        else:
            return False


class ConfirmAnswerSerializer(serializers.Serializer):
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    answer = serializers.CharField(required=True)

class GetQuestionSerializer(serializers.Serializer):
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)

class ConfirmTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    token = serializers.CharField(required=True)




class NoEmailLoginSerializer(LoginSerializer):
    email = None

