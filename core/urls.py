from django.urls import path
from . import views
from . import context_processors

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('page_not_found', views.page_not_found, name='error_404'),
    path('logout', context_processors.onLogout, name='logout'),
]
