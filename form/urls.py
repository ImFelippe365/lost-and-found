from django.urls import path
from . import views

urlpatterns = [
    path('items/create', views.create_post, name='items/create'),
]