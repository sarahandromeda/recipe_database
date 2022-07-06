from django.contrib import admin
from .models import Diet, Cuisine, Difficulty, CookTime, Ingredient, PrepMethod, QuantityUnit, Recipie, RecipieIngredient 

# Register your models here.
admin.site.register(Diet)
admin.site.register(Cuisine)
admin.site.register(Difficulty)
admin.site.register(CookTime)
admin.site.register(Ingredient)
admin.site.register(PrepMethod)
admin.site.register(QuantityUnit)
admin.site.register(Recipie)
admin.site.register(RecipieIngredient)