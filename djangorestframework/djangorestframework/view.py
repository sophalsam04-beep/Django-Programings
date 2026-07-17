  # CRUD Operatinos
  
from rest_framework import generics
from .model import Product
from .serializer import ProductSerializer


   # CREATE + READ ALL
class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # READ ONE + UPDATE + DELETE
    
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
