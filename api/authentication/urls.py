from django.urls import path
from .views import UserRegistration, UserLogin, UserLogout
from django.views.decorators.csrf import csrf_exempt  # Import csrf_exempt


urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user-registration'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('logout/', UserLogout.as_view(), name='user-logout'),
    # path('forgot-password/', forgot_password.as_view(), name='forgot-password'),
    # path('reset-password/', ResetPassword.as_view(), name='reset-password'),
]
