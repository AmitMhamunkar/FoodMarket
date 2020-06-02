from django.shortcuts import render,redirect
from foodapp.models import FoodModel
from foodapp.forms import FoodForm
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers 
import json
def filterFoodbyname(request,name):
	data=serializers.serialize('json',FoodModel.objects.filter(name__contains=name))
	print(data)
	d=json.loads(data.replace('/',''))
	return JsonResponse({'food':d})
	

# Create your views here.
def showAllFoodsView(request):
	foods=FoodModel.objects.all()
	return render(request,'foodapp/foods.html',{'allfoods':foods})

def deleteFoodByIdView(request,id):
	print('deleteFoodByIdView')
	foundFood=FoodModel.objects.get(id=id)
	foundFood.delete()
	return redirect('/foodapp/foods')

def createFoodView(request):
	form=FoodForm()
	if request.method == 'POST':
		form=FoodForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/foodapp/foods')
	return render(request,'foodapp/addfood.html',{'form':form})

def updateFoodByIdView(request,id):
	print('IN UPDATE')
	foundFood=FoodModel.objects.get(id=id)
	form=FoodForm(instance=foundFood)
	if request.method == 'POST':
		form=FoodForm(request.POST,instance=foundFood)
		if form.is_valid():
			form.save()
			return redirect('/foodapp/foods')
	return render(request,'foodapp/updatefood.html',{'form':form})

	
