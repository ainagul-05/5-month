from django.urls import path, include
from django.contrib import admin
from .views import CategoryListView, CategoryDetailView, ProductListView, ProductDetailView, ReviewListView, ReviewDetailView , ProductWithReviewsView

urlpatterns = [
        path('categories/',CategoryListView.as_view()),
        path('categories/<int:pk>/', CategoryDetailView.as_view()),
        path('products/', ProductListView.as_view()),
        path('products/<int:pk>/', ProductDetailView.as_view()),
        path('reviews/', ReviewListView.as_view()),
        path('reviews/<int:pk>/', ReviewDetailView.as_view()),
        path('products/<int:pk>/reviews/', ProductWithReviewsView.as_view()),
    ]
   


 