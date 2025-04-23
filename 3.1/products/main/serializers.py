from rest_framework import serializers

from .models import Review, Product


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['product', 'text', 'mark', 'created_at']
    # реализуйте все поля
    pass


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price']



class ProductDetailsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  # предполагается, что related_name='reviews'

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'reviews']
    # реализуйте поля title, description, price и reviews (список отзывов к товару)

