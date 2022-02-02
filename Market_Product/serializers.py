from rest_framework import serializers
from .models import Product

class FullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductMinimalSerializers(serializers.ModelSerializer):
    # non_field = serializers.SerializerMethodField()  # no corresponding model property.
    class Meta:
        model = Product
        fields = ['id','title','price','sizes']