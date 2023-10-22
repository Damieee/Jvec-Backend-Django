from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer
from .models import MyCustomUser
import json

class UserRegistration(APIView):
    @csrf_exempt
    def post(self, request):
        data = json.loads(request.body)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'User registered successfully.'}, status=201)
        return JsonResponse(serializer.errors, status=400)

class UserLogin(APIView):
    @csrf_exempt
    def post(self, request):
        data = json.loads(request.body) 
        # Try to find a user with the given email
        user = MyCustomUser.objects.filter(email=data['email']).first()

        if user:
            # Check if the provided password matches the user's password
            if user.check_password(data['password']):
                login(request, user)

                try:
                    auth_token = user.generate_auth_token()
                except Exception:
                    return JsonResponse({'message': 'Error occured.'}), 500

                return JsonResponse({'message': 'User logged in Successfully.', 'data': {'token': auth_token}}, status=200)
        
        return JsonResponse({'message': 'Invalid login credentials.'}, status=400)


class UserLogout(APIView):
    @csrf_exempt
    def post(self, request):
        logout(request)
        return JsonResponse({'message': 'User logged out successfully.'}, status=200)