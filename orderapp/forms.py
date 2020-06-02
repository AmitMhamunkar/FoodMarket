from django import forms
from orderapp.models import OrderModel

# Create your tests here.
class OrderForm(forms.ModelForm):
	class Meta:
		model=OrderModel
		fields="__all__"