   # DeSerializer -> client send to Json

from .serializer import ProductSerializer

data = {
    "name" : "Un virak",
    "age" : 22,
    "email" : "samsophal@gmail.com",
};

serializer = ProductSerializer(data = data)  # Productserializer accept json data

if serializer.is_valid():
    product = serializer.save();
    
    


class ProductSerializer(serializer.ModelSerialzer):
    
    class Meta:
        model = product
        field = "__all__"
    
    
    def validate_age(self, value):
        if value < 18:
            raise serializer.validate_age(
                "Age must be at least 18 "
                )
        return value
        
