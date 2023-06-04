from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartSerializer, CartItemSerializer
from .models import CartInfo, Cart, CartItem
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class CartAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    # Create Cart
    def post(self, request, format=None):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created'}, 
                            status = status.HTTP_201_CREATED)
        return Response(serializer.errors, 
                        status = status.HTTP_400_BAD_REQUEST)
    
    # Get all cart objects
    def get(self, request, format=None):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)


class CartAPIView2(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
     # Retrive a single cart
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None: 
            cart = Cart.objects.get(id=id)
            serializer = CartSerializer(cart)
            return Response(serializer.data)

    # Complete cart update
    def put(self, request, pk, format=None):
        id = pk
        cart = Cart.objects.get(pk=id)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data updated'})
        return Response(serializer.errors, 
                        status = status.HTTP_400_BAD_REQUEST)

    # Partial cart update
    def patch(self, request, pk, format=None):
        id = pk
        cart = Cart.objects.get(pk=id)
        serializer = CartSerializer(cart, data=request.data, 
                                       partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data updated'})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # cart Delete 
    def delete(self, request, pk, format=None):
        id = pk
        cart = Cart.objects.get(pk=id)
        cart.delete()
        return Response({'msg': 'Data Deleted'}) 


class CartItemAPIView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    # Create Cartitem
    def post(self, request, format=None):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created'}, 
                            status = status.HTTP_201_CREATED)
        return Response(serializer.errors, 
                        status = status.HTTP_400_BAD_REQUEST)
    
    # Get all cartItem objects
    def get(self, request, format=None):
        cartitems = CartItem.objects.all()
        serializer = CartItemSerializer(cartitems, many=True)
        return Response(serializer.data)


class CartItemAPIView2(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
     # Retrive a single cartItem
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None: 
            cartitem = CartItem.objects.get(id=id)
            serializer = CartItemSerializer(cartitem)
            return Response(serializer.data)

    # Complete cartItem update
    def put(self, request, pk, format=None):
        id = pk
        cartitem = CartItem.objects.get(pk=id)
        serializer = CartItemSerializer(cartitem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data updated'})
        return Response(serializer.errors, 
                        status = status.HTTP_400_BAD_REQUEST)

    # Partial cartItem update
    def patch(self, request, pk, format=None):
        id = pk
        cartitem = CartItem.objects.get(pk=id)
        serializer = CartItemSerializer(cartitem, data=request.data, 
                                       partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data updated'})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # cartItem Delete 
    def delete(self, request, pk, format=None):
        id = pk
        cartitem = CartItem.objects.get(pk=id)
        cartitem.delete()
        return Response({'msg': 'Data Deleted'}) 
