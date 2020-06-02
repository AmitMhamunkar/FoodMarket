from django import forms
from foodapp.models import FoodModel

class FoodForm(forms.ModelForm):
	class Meta:
		model=FoodModel
		fields='__all__'