from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my_home/', views.my_home, name='my_home'),
    path('create/', views.create, name='create'),
    path('edit/<int:recipe_id>/', views.edit, name='edit'),
    path('<int:recipe_id>/', views.recipe, name='recipe')
]