from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        null=True
    )
    REQUIRED_FIELDS = ['email']

    reset_token = models.CharField(
        max_length=6,
        null=True,
        blank=True
    )

    phone_number = models.CharField(
        max_length=32,
        null=True,
        blank=True
    )


class Question(models.Model):
    question = models.CharField(
        max_length = 250,
        unique=True,
        null = False,
        blank = False
    )

    def __str__(self):
        return self.question


class Profile(models.Model):
    GENDER_CHOICES = (
        ('U', 'UNKNOWN'),
        ('M', 'MALE'),
        ('F', 'FEMALE')
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    bg_img = models.URLField(
        null=True,
        blank=True
    )

    first_name = models.CharField(
        max_length=45,
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=45,
        null=True,
        blank=True
    )

    gender = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=GENDER_CHOICES
    )


    question = models.ForeignKey(
        Question,
        null = True,
        blank = True
    )

    answer = models.CharField(
        max_length = 150,
        null = True,
        blank = True
    )

    def __str__(self):
        return (self.first_name if self.first_name else  str(self.id)) + ' ' + (self.last_name if self.last_name else '')



class Message(models.Model):
    text = models.TextField(
        blank=True,
        null=True
    )

    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="messages_sent"
    )

    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="messages_received",
        null=True,
        blank=True
    )

    image = models.BooleanField()
    
    image_extension = models.CharField(
        blank=True,
        null=True,
        max_length=10
    )

    inserted_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )
