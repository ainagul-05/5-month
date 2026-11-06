from rest_framework import serializers
from django.db.models import Avg

from .models import Category, Product, Review




class CategorySerializer(serializers.ModelSerializer):

    products_count = serializers.SerializerMethodField()

    def get_products_count(self, obj):
        return obj.products.count()

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Название категории не может быть пустым"
            )
        return value.strip()

    class Meta:
        model = Category
        fields = '__all__'




class ProductSerializer(serializers.ModelSerializer):

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Название товара не может быть пустым"
            )
        return value.strip()

    def validate_description(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Описание товара не может быть пустым"
            )
        return value.strip()

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Цена должна быть больше нуля"
            )
        return value

    class Meta:
        model = Product
        fields = '__all__'




class ReviewSerializer(serializers.ModelSerializer):

    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Текст отзыва не может быть пустым"
            )
        return value.strip()

    def validate_stars(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError(
                "Оценка должна быть от 1 до 5"
            )
        return value

    class Meta:
        model = Review
        fields = '__all__'




class ProductWithReviewsSerializer(serializers.ModelSerializer):

    reviews = ReviewSerializer(many=True, read_only=True)

    average_rating = serializers.SerializerMethodField()

    def get_average_rating(self, obj):
        return obj.reviews.aggregate(
            avg=Avg('stars')
        )['avg']

    class Meta:
        model = Product
        fields = '__all__'