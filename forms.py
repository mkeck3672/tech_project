from django import forms
from .models import RecipeInfo

class RecipeInfoForm(forms.ModelForm):

	class Meta:
		model = RecipeInfo
		fields = ('recipe_name', 'recipe_content',)

class RecipeInfoDeleteForm(forms.ModelForm):
	
	class Meta:
		model = RecipeInfo
		fields = ('recipe_name',)

class RecipeInfoFindForm(forms.ModelForm):

	class Meta:
		model = RecipeInfo
		fields = ('recipe_name',)
