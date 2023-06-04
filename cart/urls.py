from django.urls import path
from .views import (CartAPIView, CartAPIView2, CartItemAPIView, 
CartItemAPIView2)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('cart/', CartAPIView.as_view()),
    path('cart/<int:pk>/', CartAPIView2.as_view()),
    path('cartitem/', CartItemAPIView.as_view()),
    path('cartitem/<int:pk>/', CartItemAPIView2.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)