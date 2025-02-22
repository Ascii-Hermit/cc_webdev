from django.urls import path
from .views import check_promotion

urlpatterns = [
    path('', check_promotion, name='check_promotion'),
]
