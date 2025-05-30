from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer

from main.models import Product


@api_view(['GET'])
def products_list_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        ser = ProductListSerializer(products,many=True)
        return Response(ser.data)
    else:
        return Response('Поддерживаются исключительно GET запросы')
    # """реализуйте получение всех товаров из БД
    # реализуйте сериализацию полученных данных
    # отдайте отсериализованные данные в Response"""



class ProductDetailsView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise NotFound("Продукт с таким ID не найден")

        serializer = ProductDetailsSerializer(product)
        return Response(serializer.data)
        """реализуйте получение товара по id, если его нет, то выдайте 404
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        pass


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        pass
