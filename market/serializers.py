from rest_framework import serializers 
from .models import Category, Product, Review
class CategorySerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Category 
        fields = 'all'
class ProductSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Product
        fields = 'all'
class ReviewSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Review 
        fields = 'all'