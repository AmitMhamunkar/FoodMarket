from django import forms
from userapp.models import UserModel

class Userform(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=UserModel
		fields='__all__'

