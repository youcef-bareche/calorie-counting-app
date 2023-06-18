from django.contrib import admin
from django.urls import path, include
from .views import list_foods, get_food

urlpatterns = [
    path('', list_foods, name='foods'),
    path('food/<int:pk>/', get_food, name='food'),
]