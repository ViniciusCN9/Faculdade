from django.urls import path, include
from .views import BookViewSet

urlpatterns = [
    path('', BookViewSet.as_view())
]