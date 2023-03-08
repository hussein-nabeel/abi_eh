from rest_framework import serializers
from .models import Prodect


class ProdectSerializer(serializers.ModelSerializer):
    image= serializers.ImageField(required=False)
    
    class Meta:
        model = Prodect
        fields=['id','category','title','description','price','created_at','image']