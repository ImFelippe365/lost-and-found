from django.urls import path, include
from . import views

urlpatterns = [
    path('all-registers', views.allRegisters, name='all-registers'),
    path('all-registers/details', views.details, name='details'),
    #path('all-registers/details/<int:register_id>', views.details, name='details'),
]
