from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.services.api.serializers import *
from apps.services.models import Category, Cart, Product


@api_view(['GET'])
def categories(request):
    categories = Category.objects.all()
    categories_serializer = CategorySerializer(categories, many=True)
    response = {
        'code': 101,
        'message': 'Successful',
        'data': categories_serializer.data,
    }
    return Response(response)


@api_view(['GET', 'POST'])
def cart(request):
    try:
        if request.method == 'POST':
            data = request.data
            product_id = data.get('productId', 1)
            quantity = data.get('quantity', 1)
            product = Product(id=product_id)
            cart = Cart(product=product, quantity=quantity)
            cart.save()

            response = {
                'code': 102,
                'message': 'Object created',
                'data': [],
            }
            return Response(response, status=status.HTTP_201_CREATED)
        elif request.method == 'GET':
            cart = Cart.objects.all()
            cart_serializer = CartSerializer(cart, many=True)
            response = {
                'code': 101,
                'message': 'Successful',
                'data': cart_serializer.data,
            }
            return Response(response)
    except:
        response = {
            'code': 501,
            'message': 'Error interno del servidor',
            'data': [],
        }
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

