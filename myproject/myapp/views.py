from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import views, permissions, status
from rest_framework.response import Response
from .serializers import CustomUserSerializer,RegisterSerializer
import jwt
from django.contrib.auth import authenticate

class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:
            # Generate JWT token
            token = jwt.encode({'id': user.id, 'email': user.email}, 'secret', algorithm='HS256')
            # Serialize the user object
            user_serializer = CustomUserSerializer(user)
            # Return the token and user data in the response
            return Response({'token': token, 'user': user_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        # Invalidate the token
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class RegisterView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

