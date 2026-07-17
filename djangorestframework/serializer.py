     # Serializer
        # Converting python object -> json

from rest_framework import serializers
from .model import Product
from .model import Student



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        field = "__all__"
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        field = "__all__"


