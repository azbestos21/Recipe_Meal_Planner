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
    path('recipes/<int:pk>/', views.recipe_detail, name='recipe_detail'),  # URL for recipe details
    path('schedules/', views.meal_schedule_list, name='meal_schedule_list'),
    path('schedules/create/', views.meal_schedule_create, name='meal_schedule_create'),
    path('schedules/update/<int:pk>/', views.meal_schedule_update, name='meal_schedule_update'),
    path('schedules/delete/<int:pk>/', views.meal_schedule_delete, name='meal_schedule_delete'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
