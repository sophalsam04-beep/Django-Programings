from rest_framework import serializers
from .model import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        field = "__all__"
        
        
   # Create objects
Product.objects.create(
    name = "Un virak",
    age = 22,
    email = "virakun@gmail.com",
)