from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import status

# Register User
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email', '')

        if not username or not password:
            return Response({'error': 'Username and Password required'}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'User already exists'}, status=400)

        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({'message': 'User registered successfully'}, status=201)

# Login View
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid credentials'}, status=400)

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

# Logout View (optional: token blacklisting)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=200)
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Fetch the user profile details
        user = request.user
        return Response({
            'username': user.username,
            'email': user.email,
            # Optionally, you can return more details, but not the password
        })