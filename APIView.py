    # APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ProductSerializer


class StudentCreate(APIView):
    
    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors);
    
    
    
