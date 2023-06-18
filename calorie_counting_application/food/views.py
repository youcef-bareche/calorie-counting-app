from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import FoodItem
from .serializers import FoodSerializer


# Create your views here.
@api_view()
def list_foods(request):
    foods = FoodItem.objects.all()
    food_serializer = FoodSerializer(foods, many=True)
    return Response(data=food_serializer.data)

@api_view()
def get_food(request, pk=None):
    food = FoodItem.objects.get(pk=pk)
    food_serializer = FoodSerializer(food)
    return Response(food_serializer.data)