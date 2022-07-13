from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.
class Diet(models.Model):
    diet = models.CharField('diet', max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.diet

class Cuisine(models.Model):
    cuisine = models.CharField('cuisine', max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.cuisine

class Difficulty(models.Model):
    DIFFICULTIES = (
    ('EASY', 'Beginner'),
    ('MEDIUM', 'Intermediate'),
    ('HARD', 'Advanced')
    )
    difficulty = models.CharField('difficulty', max_length=100, choices=DIFFICULTIES)

    def __str__(self):
        return self.difficulty

    class Meta:
        verbose_name = 'difficulty'
        verbose_name_plural = 'difficulties'


class CookTime(models.Model):
    COOK_TIMES = (
    ('SHORTEST', '0min - 30min'),
    ('SHORT', '30min - 1hr'),
    ('LONG', '1hr - 2hr'),
    ('LONGEST', '2hr +')
    )
    cook_time = models.CharField('cook time', max_length=100, choices=COOK_TIMES)

    def __str__(self):
        return self.cook_time

class Ingredient(models.Model):
    ingredient_name = models.CharField('ingredient', max_length=100, unique=True)

    def __str__(self):
        return self.ingredient_name

class PrepMethod(models.Model):
    prep_method = models.CharField('prep method', max_length=100, unique=True)

    def __str__(self):
        return self.prep_method

class QuantityUnit(models.Model):
    quantity_unit = models.CharField('quantity unit', max_length=100, unique=True)

    def __str__(self):
        return self.quantity_unit

class Recipe(models.Model):
    recipe_name = models.CharField('recipe name', max_length=100)
    description = models.TextField('description', max_length=200)
    instructions = models.TextField('instructions', max_length=800)
    diet = models.ManyToManyField(Diet)
    cuisine = models.ForeignKey(
        'Cuisine', 
        on_delete=models.CASCADE, 
        related_name='recipes', 
        related_query_name='recipe'
        )
    difficulty = models.ForeignKey(
        'Difficulty', 
        on_delete=models.CASCADE,
        related_name='recipes',
        related_query_name='recipe'
        )
    cook_time = models.ForeignKey(
        'CookTime', 
        on_delete=models.CASCADE,
        related_name='recipes',
        related_query_name='recipe'
        )

    def __str__(self):
        return self.recipe_name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        'Recipe', 
        on_delete=models.CASCADE,
        related_name='recipe_ingredients',
        related_query_name='recipe_ingredient'
        )
    ingredient = models.ForeignKey(
        'Ingredient', 
        on_delete=models.CASCADE,
        related_name='recipe_ingredients',
        related_query_name='recipe_ingredient'
        ) 
    quantity_unit = models.ForeignKey(
        'QuantityUnit', 
        on_delete=models.CASCADE,
        related_name='recipe_ingredients',
        related_query_name='recipe_ingredient'
        )
    prep_method = models.ForeignKey(
        'PrepMethod', 
        on_delete=models.CASCADE,
        related_name='recipe_ingredients',
        related_query_name='recipe_ingredient'
        )
    amount = models.FloatField()

    def __str__(self):
        return self.ingredient


