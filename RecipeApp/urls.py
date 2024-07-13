# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipes/create/', views.recipe_create, name='recipe_create'),
    path('recipes/update/<int:pk>/', views.recipe_update, name='recipe_update'),
    path('recipes/delete/<int:pk>/', views.recipe_delete, name='recipe_delete'),
    # Add other CRUD URLs for Recipe and MealSchedule as needed
]
