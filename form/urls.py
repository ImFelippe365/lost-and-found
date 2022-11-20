from django.urls import path
from . import views

urlpatterns = [
    path('create-post', views.create_post, name='create-post'),
]