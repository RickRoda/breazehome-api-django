from django.contrib import admin

from user.models import User, Profile, Question

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Question)
