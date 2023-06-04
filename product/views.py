from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (ProductSerializer, OrderSerializer, 
OrderItemSerializer)
from .models import Product, Order, OrderItem
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create Product API.
class ProductAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    # Create product
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created'}, 
                            status = status.HTTP_201_CREATED)
        return Response(serializer.errors, 
                        status = status.HTTP_400_BAD_REQUEST)
    
     # Get all products
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductAPIView2(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
     # Retrive a single product
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None: 
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)

    # Complete product update
    def put(self, request, pk, format=None):
        id = pk
        product = Product.objects.get(pk=id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data updated'})
        return Response(serializer.errors, 
                        status = status.HTTP_400_BAD_REQUEST)

    # Partial product update
    def patch(self, request, pk, format=None):
        id = pk
        product = Product.objects.get(pk=id)
        serializer = ProductSerializer(product, data=request.data, 
                                       partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data updated'})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # Product Delete 
    def delete(self, request, pk, format=None):
        id = pk
        product = Product.objects.get(pk=id)
        product.delete()
        return Response({'msg': 'Data Deleted'})


# Create Order API
class OrderAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    # Create Order
    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created'}, 
                            status = status.HTTP_201_CREATED)
        return Response(serializer.errors, 
                        status = status.HTTP_400_BAD_REQUEST)
    
     # Get all orders
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class OrderAPIView2(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
     # Retrive a single oredr
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None: 
            order = Order.objects.get(id=id)
            serializer = OrderSerializer(order)
            return Response(serializer.data)

    # Complete Order update
    def put(self, request, pk, format=None):
        id = pk
        order = Order.objects.get(pk=id)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data updated'})
        return Response(serializer.errors, 
                        status = status.HTTP_400_BAD_REQUEST)

    # Partial Oredr update
    def patch(self, request, pk, format=None):
        id = pk
        order = Order.objects.get(pk=id)
        serializer = OrderSerializer(Order, data=request.data, 
                                       partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data updated'})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # Order Delete 
    def delete(self, request, pk, format=None):
        id = pk
        order = Order.objects.get(pk=id)
        order.delete()
        return Response({'msg': 'Data Deleted'})


# Create OrderItem API
class OrderItemAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    # Create OrderItem
    def post(self, request, format=None):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created'}, 
                            status = status.HTTP_201_CREATED)
        return Response(serializer.errors, 
                        status = status.HTTP_400_BAD_REQUEST)
    
     # Get all ordersitems
    def get(self, request, format=None):
        orderitems = OrderItem.objects.all()
        serializer = OrderItemSerializer(orderitems, many=True)
        return Response(serializer.data)


class OrderItemAPIView2(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
     # Retrive a single oredritem
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None: 
            orderitem = OrderItem.objects.get(id=id)
            serializer = OrderItemSerializer(orderitem)
            return Response(serializer.data)

    # Complete Orderitem update
    def put(self, request, pk, format=None):
        id = pk
        orderitem = OrderItem.objects.get(pk=id)
        serializer = OrderItemSerializer(orderitem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data updated'})
        return Response(serializer.errors, 
                        status = status.HTTP_400_BAD_REQUEST)

    # Partial Oredritem update
    def patch(self, request, pk, format=None):
        id = pk
        orderitem = OrderItem.objects.get(pk=id)
        serializer = OrderItemSerializer(orderitem, data=request.data, 
                                       partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data updated'})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # Orderitem Delete 
    def delete(self, request, pk, format=None):
        id = pk
        orderitem = OrderItem.objects.get(pk=id)
        orderitem.delete()
        return Response({'msg': 'Data Deleted'})
