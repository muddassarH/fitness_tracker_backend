from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class FetchUserProfileView(APIView):
    def get(self, request):
        # Logic to retrieve user profile data
        user = request.user
        context = {
            'username': user.username,
            'email': user.email,
            'age': user.age,
            'goals': user.goals,
            'profile_picture': user.profile_picture.url if user.profile_picture else None,
            'location': user.location,
            'birth_date': user.birth_date,
        }
        return Response(context, status=status.HTTP_200_OK)
    
class CreateUserProfileView(APIView):
    def post(self, request):
        pass
