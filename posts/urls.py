from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('items', views.items, name='items'),
    path('delivered-items', views.deliveredItems, name='delivered-items'),
    path('expired-items', views.expiredItems, name='expired-items'),
    path('all-registers', views.allRegisters, name='all-registers'),
    path("__reload__/", include("django_browser_reload.urls")),
]
