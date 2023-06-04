from django.urls import path
from .views import (ProductAPIView, ProductAPIView2, 
OrderAPIView, OrderAPIView2, OrderItemAPIView, OrderItemAPIView2)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('product/', ProductAPIView.as_view()),
    path('product/<int:pk>/', ProductAPIView2.as_view()),
    path('order/', OrderAPIView.as_view()),
    path('order/<int:pk>/', OrderAPIView2.as_view()),
    path('orderitem/', OrderItemAPIView.as_view()),
    path('orderitem/<int:pk>/', OrderItemAPIView2.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)