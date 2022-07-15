from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from requests import request
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
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def create(response):
    recipe_form = CreateNewRecipe()
    ingredient_formset = IngredientFormSet(queryset=RecipeIngredient.objects.none())
    if is_ajax(response):
        term = response.GET.get('term')
        ingredients = Ingredient.objects.all().filter(ingredient_name__icontains=term)
        response_content = list(ingredients.values())
        return JsonResponse(response_content, safe=False)
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
