from django.urls import path, include
from . import views

urlpatterns = [
    path('items/', views.items, name='items'),
    path('delivered-items', views.deliveredItems, name='delivered-items'),
    path('expired-items', views.expiredItems, name='expired-items'),
    path('items/create', views.create_post, name='items/create'),
    path('items/complete-delivery', views.complete_delivery, name='complete-delivery'),
]
