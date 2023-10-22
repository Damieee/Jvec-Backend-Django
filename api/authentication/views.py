from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer
from .models import MyCustomUser
import json

class UserRegistration(View):
    @csrf_exempt
    def post(self, request):
        data = json.loads(request.body)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'User registered successfully.'}, status=201)
        return JsonResponse(serializer.errors, status=400)

class UserLogin(View):
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


class UserLogout(View):
    @csrf_exempt
    def post(self, request):
        logout(request)
        return JsonResponse({'message': 'User logged out successfully.'}, status=200)

# class ForgotPassword(View):
#     @csrf_exempt
#     def post(self, request):
#         data = json.loads(request.body)
#         email = data['email']
#         if not email:
#             return JsonResponse({'message': 'Invalid email.'}, status=400)
#         user = User.objects.filter(email=email).first()
#         if not user:
#             return JsonResponse({'message': 'Invalid email. Please try again.'}, status=400)
#         reset_token = token.send_token(email=email)
#         # Send the reset token via email (you can implement this)
#         return JsonResponse({'message': 'An email containing instructions to reset your password has been sent.'}, status=200)

# class ResetPassword(View):
#     @csrf_exempt
#     def post(self, request):
#         data = json.loads(request.body)
#         email = data['email']
#         reset_token = data['token']
#         new_password = data['new_password']
#         confirm_password = data['confirm_password']
#         if not email:
#             return JsonResponse({'message': 'Email cannot be empty.'}, status=400)
#         user = User.objects.filter(email=email).first()
#         if not user:
#             return JsonResponse({'message': 'Invalid email. Please try again.'}, status=401)
#         if reset_token != new_token:
#             return JsonResponse({'message': 'Invalid Token. Please try again.'}, status=401)
#         if not new_password:
#             return JsonResponse({'message': 'New password cannot be empty.'}, status=400)
#         if new_password != confirm_password:
#             return JsonResponse({'message': 'The passwords you entered do not match. Please make sure that both passwords are the same.'}, status=400)
#         user.set_password(new_password)
#         user.save()
#         return JsonResponse({'message': 'Password successfully changed.'}, status=200)
