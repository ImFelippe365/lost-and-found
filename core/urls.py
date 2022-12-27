from django.urls import path
from . import views
from . import context_processors

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout:<int:id>', context_processors.onLogout, name='logout'),
]
