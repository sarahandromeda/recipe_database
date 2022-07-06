from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my_home/', views.my_home, name='my_home'),
    path('create/', views.create, name='create'),
    path('edit/', views.edit, name='edit'),
    path('<int:recipie_id>/', views.recipie, name='recipie')
]