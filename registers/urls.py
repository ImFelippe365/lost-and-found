from django.urls import path, include
from . import views

urlpatterns = [
    path('all-registers', views.allRegisters, name='all-registers'),
    path('<int:register_id>', views.details, name='details'),
]
