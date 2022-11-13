from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('itens', views.itens, name='itens'),
    path("__reload__/", include("django_browser_reload.urls")),
]
