from django.urls import path, include
from . import views

urlpatterns = [
    path('items/', views.ItemsView.as_view(), name='items'),
    path('delivered-items', views.DeliveredItemsView.as_view(), name='delivered-items'),
    path('expired-items', views.ExpiredItemsView.as_view(), name='expired-items'),
    path('items/create', views.CreateItem.as_view(), name='items/create'),
    path('items/<int:pk>/delete/', views.DeleteItem.as_view(), name='delete'),
    path('items/update/<int:pk>', views.UpdateItem.as_view(), name='edit-item'),
    path('items/complete-delivery/<int:pk>', views.CompleteDelivery.as_view(), name='complete-delivery'),
]
