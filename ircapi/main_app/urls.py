from django.urls import path
from . import views

urlpatterns = [
    path('connections/', views.connection_list),
]