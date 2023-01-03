from django.urls import path, include
from . import views

urlpatterns = [
    path('registers', views.Registers.as_view(), name='registers'),
    # path('registers/details', views.details, name='details'),
    path('registers/<int:pk>/details', views.RegisterDetails.as_view(), name='details'),
]
