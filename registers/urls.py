from django.urls import path, include
from . import views

urlpatterns = [
    path('registers', views.RegistersView.as_view(), name='registers'),
    path('registers/search', views.RegistersSearchResultsView.as_view(), name='registers-search'),
    # path('registers/details', views.details, name='details'),
    path('registers/<int:pk>/details', views.RegisterDetailsView.as_view(), name='details'),
]
