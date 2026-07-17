from django.urls import path
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
);

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import AllowAny   # Permission consist who that one acessing it
from rest_framework.permissions import IsAuthenticated

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view()),  # API Token
    path("api/token/refresh/", TokenRefreshView.as_view())  # API Refresh token
];


permission_class = [AllowAny];

  # Login Required -> before you used you can login here
  
permission_class = [IsAuthenticated];

   # Admin only
   
permission_class = [IsAdminUser];


   # GET -> READ
permission_class = [IsAuthenticatedOrReadOnly];