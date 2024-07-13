from django import forms
from .models import Recipe, MealSchedule

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'instructions']

class MealScheduleForm(forms.ModelForm):
    class Meta:
        model = MealSchedule
        fields = ['recipe', 'date', 'meal_type']
