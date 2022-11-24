from django.urls import path
from . import views

urlpatterns = [
    path('items/create', views.create_post, name='items/create'),
    path('items/complete-delivery', views.complete_delivery, name='complete-delivery'),
]