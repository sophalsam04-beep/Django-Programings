from django.urls import path
from .view import ProductListCreate, ProductDetail
from django.urls import include, path

urlpatterns = [
    path("products/", ProductListCreate.as_view()),
    path("products/<int:pk>/", ProductDetail.as_view())
];

urlpatterns = [
    path("api/", include("products.urls")),

];



