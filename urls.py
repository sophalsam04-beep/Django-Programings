from django.urls import path
from .view import ProductList


urlpatterns = [
    path("products/", ProductList.as_view())
];