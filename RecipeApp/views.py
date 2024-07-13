from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Recipe, MealSchedule
from .forms import RecipeForm, MealScheduleForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def dashboard_view(request):
    recipes = Recipe.objects.filter(user=request.user)
    schedules = MealSchedule.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'recipes': recipes, 'schedules': schedules})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def recipe_list(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'recipe_list.html', {'recipes': recipes})

@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipe_form.html', {'form': form})

@login_required
def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, user=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe_form.html', {'form': form})

@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, user=request.user)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'recipe_confirm_delete.html', {'recipe': recipe})

@login_required
def meal_schedule_list(request):
    schedules = MealSchedule.objects.filter(user=request.user)
    return render(request, 'meal_schedule_list.html', {'schedules': schedules})

@login_required
def meal_schedule_create(request):
    if request.method == 'POST':
        form = MealScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.user = request.user
            schedule.save()
            return redirect('meal_schedule_list')
    else:
        form = MealScheduleForm()
    return render(request, 'meal_schedule_form.html', {'form': form})

@login_required
def meal_schedule_update(request, pk):
    schedule = get_object_or_404(MealSchedule, pk=pk, user=request.user)
    if request.method == 'POST':
        form = MealScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('meal_schedule_list')
    else:
        form = MealScheduleForm(instance=schedule)
    return render(request, 'meal_schedule_form.html', {'form': form})

@login_required
def meal_schedule_delete(request, pk):
    schedule = get_object_or_404(MealSchedule, pk=pk, user=request.user)
    if request.method == 'POST':
        schedule.delete()
        return redirect('meal_schedule_list')
    return render(request, 'meal_schedule_confirm_delete.html', {'schedule': schedule})
