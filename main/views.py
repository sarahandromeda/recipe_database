from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Diet, Cuisine, Difficulty, CookTime, Ingredient, PrepMethod, QuantityUnit, Recipe, RecipeIngredient 
from .forms import CreateNewRecipe, IngredientFormSet

# Create your views here.
# main home page
# show 3 random recipes
# search bar
# login link
# if user signed in, show user home page link
def home(response): 
    return render(response, 'main/home.html', {})

# user home page
# show list of created repicies
# buttons to delete or edit
# if no one signed in, show sign in link
def my_home(response): 
    return render(response, 'main/user_home.html', {})

# create new recipe page
# show recipe form
def create(response):
    recipe_form = CreateNewRecipe()
    ingredient_formset = IngredientFormSet(queryset=RecipeIngredient.objects.none())
    return render(
        response, 
        'main/create.html', 
        {'recipe_form': recipe_form, 'ingredient_formset': ingredient_formset}
        )

# edit recipe page
# show edit form populated with currect recipe data
def edit(response, id): 
    return render(response, 'main/edit.html', {})

# recipe page
# show recipe information
# add button to show random recipe
def recipe(response, id):
    return render(response, 'main/recipe_page.html', {})
