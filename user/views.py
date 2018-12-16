import json
import re

from rest_framework import viewsets
from user.models import User, Question
from user.serializers import (
    UserSerializer,
    QuestionSerializer,
    PasswordResetSerializer,
    PasswordResetConfirmSerializer,
    NewPasswordSerializer,
    ConfirmAnswerSerializer,
    ConfirmTokenSerializer,
    GetQuestionSerializer,
    )
from real_estate.serializers import PropertyTagSerializer
from real_estate.models import Tag
from rest_framework import generics, status
from rest_framework.response import Response
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template import loader
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from breaze.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.db.models.query_utils import Q
from django.utils import crypto
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import AllowAny
from django.core.signing import Signer

class UserTagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tags to be viewed or edited.
    """
    serializer_class = PropertyTagSerializer
    ordering_fields = '__all__'

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        pk = self.kwargs['user_pk']
        return Tag.objects.filter(uid=pk)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class UserUpdateView(generics.GenericAPIView, UpdateModelMixin):
    '''
    Book update API, need to submit both `name` and `author_name` fields
    At the same time, or django will prevent to do update for field missing
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class UserPartialUpdateView(generics.GenericAPIView, UpdateModelMixin):
    '''
    You just need to provide the field which is to be modified.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

# #2426 Ronny Alfonso ralfo040@fiu.edu
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny,]
# end block #2426

class ResetPasswordRequestView(generics.GenericAPIView):
        #renderer_classes = [TemplateHTMLRenderer]
        #template_name = "account/password_reset_form.html"    #code for template is given below the view's code
        #success_url = 'password_reset_done'
        serializer_class = PasswordResetSerializer
        permission_classes = [ AllowAny, ]
        #form_class = PasswordResetRequestForm

        @staticmethod
        def validate_email_address(email):
        #This method here validates the if the input is an email address or not. Its return type is boolean, True if the input is a email address or False if its not.
            try:
                validate_email(email)
                return True
            except ValidationError:
                return False

        def generate_random_token(self):
            #TODO: Change user model:  add a "reset_token" attribute. Use this function to create the string.  Save the string to reset_token.
            #TODO: Disable CSRF. Create the token in the post method.  Add the token to the email dictionary.  Be able to send the email.
            #TODO: Frontend should have a form to enter the code.  The code gets appended to the reset_password_confirm url and gets checked against the database.
            token = crypto.get_random_string(length=5, allowed_chars='1234567890')
            #user.objects.get(.update(reset_token=token)
            return token

        def post(self, request, *args, **kwargs):
        #A normal post request which takes input from field "email_or_username" (in ResetPasswordRequestForm).

            #form = self.form_class(request.POST)
            #if form.is_valid():
            #    data= form.cleaned_data["email_or_username"]
            #    import pdb; pdb.set_trace();
            reg=re.compile('^[-+]?[0-9]+$')
            if request.method == "POST":
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                data = body['email']

            if self.validate_email_address(data) is True:                 #uses the method written above
                '''
                If the input is an valid email address, then the following code will lookup for users associated with that email address. If found then an email will be sent to the address, else an error message will be printed on the screen.
                '''
                associated_users= User.objects.filter(Q(email=data)|Q(username=data))
                if associated_users.exists():
                    for user in associated_users:
                        #TODO:Generate token here;
                        token = self.generate_random_token()
                        user.reset_token = token
                        user.save()
                        c = {
                            'email': user.email,
                            'domain': request.META['HTTP_HOST'],
                            'site_name': 'breazehome.com',
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'user': user,
                            'token': token,
                            'protocol': 'http',
                            }
                        subject_template_name='registration/password_reset_subject.html'
                        # copied from django/contrib/admin/templates/registration/password_reset_subject.txt to templates directory
                        email_template_name='registration/password_reset_email.html'
                        # copied from django/contrib/admin/templates/registration/password_reset_email.html to templates directory
                        subject = loader.render_to_string(subject_template_name, c)
                        # Email subject *must not* contain newlines
                        subject = ''.join(subject.splitlines())
                        email = loader.render_to_string(email_template_name, c)
                        #TODO: send_mail's return type is a boolean.  0 if message not sent, 1 if message is sent.  Test this out to make sure that the e-mails are actually getting sent.
                        send_mail(subject, email, EMAIL_HOST_USER , [user.email], fail_silently=False)
                    messages.success(self.request._request, 'An email has been sent to ' + data +". Please check its inbox to continue reseting password.")
                    return Response({"detail": "Password reset e-mail has been sent."}, status=status.HTTP_200_OK)
                messages.error(self.request._request, 'No user is associated with this email address')
                return Response({"detail": "No user is associated with this email address."}, status=status.HTTP_404_NOT_FOUND)
            else:
                '''
                If the input is an username, then the following code will lookup for users associated with that user. If found then an email will be sent to the user's address, else an error message will be printed on the screen.
                '''
                associated_users= User.objects.filter(username=data)
                if associated_users.exists():
                    for user in associated_users:
                        token = self.generate_random_token()
                        user.reset_token = token
                        user.save()
                        c = {
                            'email': user.email,
                            'domain': 'breazehome.com', #or your domain
                            'site_name': 'example',
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'user': user,
                            'token': token,
                            'protocol': 'http',
                            }
                        subject_template_name='registration/password_reset_subject.html'
                        email_template_name='registration/password_reset_email.html'
                        subject = loader.render_to_string(subject_template_name, c)
                        # Email subject *must not* contain newlines
                        subject = ''.join(subject.splitlines())
                        email = loader.render_to_string(email_template_name, c)
                        send_mail(subject, email, EMAIL_HOST_USER , [user.email], fail_silently=False)
                    result = self.form_valid(form)
                    messages.success(self.request._request, 'An email has been sent to ' + data +". Please check its inbox to continue reseting password.")
                    return Response({"detail": "Password reset e-mail has been sent."}, status=status.HTTP_200_OK)
                messages.error(self.request._request, 'No user is associated with this email address')
                return Response({"detail": "No user is associated with that email."}, status=status.HTTP_404_NOT_FOUND)
            messages.error(self.request._request, 'Invalid Input')
            return Response({"detail": "Invalid Input"})
            #return JsonResponse({'message': "This is only temporary."})

class PasswordResetConfirmView(generics.GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer

    @staticmethod
    def validate_email_address(email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    def post(self, request, uidb64=None, token=None, *arg, **kwargs):
        UserModel = User
        if request.method == "POST":
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            token = body['token']
            email = body['email']

        try:
            if self.validate_email_address(email):
                    user = UserModel._default_manager.get(email=email)
            else:
                    user = UserModel._default_manager.get(username=email)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            user = None

        if user is not None and user.reset_token==token:
            return Response({"detail": "User confirmed"}, status=status.HTTP_200_OK)
        return Response({"detail": "This is not the user you are looking for"}, status=status.HTTP_403_FORBIDDEN)


class PasswordResetChangeView(generics.GenericAPIView):
    #template_name = "account/password_change_form.html"
    #success_url = 'password_change_done'
    #form_class = SetPasswordForm
    serializer_class = NewPasswordSerializer
    permission_classes = [ AllowAny, ]

    @staticmethod
    def validate_email_address(email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    @staticmethod
    def validate_password(new_password, new_password2):
        if new_password==new_password2:
            return True
        else:
            return False

    def post(self, request, uidb64=None, token=None, *arg, **kwargs):
        """
        View that checks the hash in a password reset link and presents a
        form for entering a new password.
        """
        UserModel = User
        #form = self.form_class(request.POST)
        #TODO:  Clean up the email template.
        #TODO(in the code below):  be sure to throw an error for no 'email' in the requesst body.  In the current implementation, the system just throws 500.

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email = body['email']
        new_password = body['new_password']

        try:
            uid = urlsafe_base64_decode(uidb64)
            if self.validate_email_address(email):
                user = UserModel._default_manager.get(email=email)
            else:
                user = UserModel._default_manager.get(username=email)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            user = None

        if user is not None: #and self.validate_password(new_password, new_password2):
            if request.method == "POST":

                new_password = body['new_password']
                user.set_password(new_password)
                user.save()
                #messages.success(self.request, 'Password has been reset.')
                return Response({"detail": "Password has been reset."}, status=status.HTTP_200_OK)
            else:
                #messages.error(self.request, 'Password reset has not been successful.')
                return Response({"detail": "Password reset was not sucessful. Please contact administrator."}, status=status.HTTP_403_FORBIDDEN)
        else:
            #messages.error(self.request,'The reset password link is no longer valid.')
            return Response({"detail": "The reset password link is no longer valid."}, status=status.HTTP_403_FORBIDDEN)


# Used to check if the email and the security question-answer match
# if match return 200 otherwise 404
class ConfirmAnswerView(generics.GenericAPIView):
    serializer_class = ConfirmAnswerSerializer
    permission_classes = [ AllowAny, ]


    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email = body['email']
        answer = "".join(body['answer'].split()).lower()
        try:
            user = User.objects.get(email=email)
            if Signer().sign(answer).split(':', 1)[1] != user.profile.answer:
                raise
        except:
            return Response({"detail": ""}, status=status.HTTP_404_NOT_FOUND)

        return Response({"detail": ""}, status=status.HTTP_200_OK)



# Used to check if the email and the token match
# if match return 200 otherwise 404
class ConfirmTokenView(generics.GenericAPIView):
    serializer_class = ConfirmTokenSerializer
    permission_classes = [ AllowAny, ]

    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email = body['email']
        token = body['token'].strip()

        try:
            user = User.objects.get(email=email)
            if user.reset_token != token or user.profile.answer == '' or user.profile.question == None :
                raise
        except:
            return Response({"detail": ""}, status=status.HTTP_404_NOT_FOUND)

        return Response({"detail": user.profile.question.question}, status=status.HTTP_200_OK)

# Used to retrieve the question that the user used to register
# if email match return 200 otherwise 404
class GetQuestionView(generics.GenericAPIView):
    serializer_class = GetQuestionSerializer
    permission_classes = [ AllowAny,]

    def post(self, request, *args, **kwargs):
        email = request.body.decode('utf-8')
        try:
            user = User.objects.get(email=email)
        except:
            return Response({'detail': ''}, status=status.HTTP_404_NOT_FOUND)
        return Response({'detail': user.profile.question.question}, status=status.HTTP_200_OK)

