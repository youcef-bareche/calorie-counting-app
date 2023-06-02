from django.db import models
from account.models import CustomUser

# Create your models here.
class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField(default=0)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    carbs = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    fat = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    fiber = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=100.0)
    image = models.ImageField(upload_to="food_items", blank=True, null=True)

    def __str__(self):
        return self.name

class FoodEntry(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    calories = models.PositiveIntegerField(default=0)

    def get_default_weight(self):
        if self.food_item:
            return self.food_item.weight
        return None

    def save(self, *args, **kwargs):
        if self.weight is None:
            self.weight = self.get_default_weight()
        super().save(*args, **kwargs)