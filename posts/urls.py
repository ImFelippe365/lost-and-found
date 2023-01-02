from django.urls import path, include
from . import views

urlpatterns = [
    path('items/', views.ItemView.as_view(), name='items'),
    path('delivered-items', views.deliveredItems, name='delivered-items'),
    path('expired-items', views.expiredItems, name='expired-items'),
    path('items/create', views.ItemCreate.as_view(), name='items/create'),
    # path('items/1/delete', views.DeleteView.as_view(), name='delete'),
    path('items/1/delete', views.tempDelete, name='delete'),
    path('items/complete-delivery', views.complete_delivery, name='complete-delivery'),
]
