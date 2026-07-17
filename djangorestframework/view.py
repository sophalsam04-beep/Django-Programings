   # View
      # Accept request and send respone

from rest_framework import generics
from .model import Product
from .model import Student
from serializer import ProductSerializer
from serializer import StudentSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all();
    serializer_class = ProductSerializer
    

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer