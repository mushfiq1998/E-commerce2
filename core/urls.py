from django.urls import path
from .views import TestAPIView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('core/', TestAPIView.as_view()), 
]
urlpatterns = format_suffix_patterns(urlpatterns)