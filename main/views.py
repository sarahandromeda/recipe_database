from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Diet, Cuisine, Difficulty, CookTime, Ingredient, PrepMethod, QuantityUnit, Recipie, RecipieIngredient 

# Create your views here.
# main home page
# show 3 random recipies
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

# create new recipie page
# show recipie form
def create(response): 
    return render(response, 'main/create.html', {})

# edit recipie page
# show edit form populated with currect recipie data
def edit(response, id): 
    return render(response, 'main/edit.html', {})

# recipie page
# show recipie information
# add button to show random recipie
def recipie(response, id):
    return render(response, 'main/recipie_page.html', {})
