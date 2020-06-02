from django import forms
from cartapp.models import CartModel

class CartForm(forms.ModelForm):
	class Meta:
		model = CartModel
		fields ='__all__'