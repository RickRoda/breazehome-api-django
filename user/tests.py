from django.test import TestCase

from rest_framework.views import APIView
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer

class TestUserQuestionViewSet(APIView):
    def get(self, request, pk, answer):
        user = User.objects.get(pk=pk)
        match = user.profile.answer == answer
        return Response("Answer matched" if match else "Wrong answer")
