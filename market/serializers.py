from rest_framework import serializers 
from .models import Category, Product, Review
from  django.db.models import Avg




class CategorySerializer(serializers.ModelSerializer): 
    products_count = serializers.SerializerMethodField()
    class Meta: 
        model = Category 
        fields = 'all'

    def get_products_count(self, obj):
        return obj.products.count()

class ProductSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Product
        fields = 'all'
class ReviewSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Review 
        fields = 'all'

class ProductWithReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_average_rating(self, obj):
        return obj.review_set.aggregate(avg=Avg('stars'))['avg']

    
        