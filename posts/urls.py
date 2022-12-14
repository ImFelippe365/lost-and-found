from django.urls import path, include
from . import views

urlpatterns = [
    path('items/', views.items, name='items'),
    path('delivered-items', views.deliveredItems, name='delivered-items'),
    path('expired-items', views.expiredItems, name='expired-items'),
    path('items/create', views.ItemCreate.as_view(), name='items/create'),
    path('items/<int:id>/delete', views.DeleteView.as_view()),
    path('items/complete-delivery', views.complete_delivery, name='complete-delivery'),
    path("__reload__/", include("django_browser_reload.urls")),
]
