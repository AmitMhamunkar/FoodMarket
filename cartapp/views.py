from django.shortcuts import render,redirect
from cartapp.models import CartModel
from django.http import HttpResponse
from cartapp.forms import CartForm
from django.db import connection 
from foodapp.models import FoodModel
from django.contrib import messages
# Create your views here.

def CheckQuantitybeforeadding(request):
	foodIdfk=request.GET['foodIdfk']
	foodQuantity=request.GET['foodQuantity']
	cursor=connection.cursor()
	quantity=cursor.execute("select quantity from foodapp_foodmodel where id=%s",[foodIdfk])
	q=int(cursor.fetchone()[0])
	print(q)
	if int(q) < int(foodQuantity):
		return HttpResponse("Out of Stock",content_type='text/plain')

def totalPriceDisplay(request):
	email=request.session['email']
	cursor=connection.cursor()
	total=cursor.execute("select sum(f.price * c.foodQuantity) from foodapp_foodmodel as f inner join cart_tbl as c on f.id=c.foodIdfk and c.emailIdfk=%s",[email])
	totalprice=int(cursor.fetchone()[0])
	return HttpResponse(totalprice,content_type='text/plain')
		
def ShowAddToCartView(request,id):
	form=CartForm()
	return render(request,'cartapp/addcart.html',{'form':form,'foodIdfk':id})

def addToCartView(request):
	food_id=request.POST["foodIdfk"]
	form=CartForm()
	if request.method == 'POST':
		sessionemail=request.session['email']
		form = CartForm(request.POST)
		cart =CartModel.objects.filter(emailIdfk=sessionemail)
		food=FoodModel.objects.get(id=food_id)
		print(food)
		if(food.quantity > int(request.POST['foodQuantity'])):
			if form.is_valid():
				print("In is valid save")
				if cart.count()==0:
					form.save()
					return redirect('/foodapp/foods')
				else:
					for c in cart:
						if int(c.foodIdfk) == int(request.POST['foodIdfk']):
							cursor=connection.cursor()
							newQuantity=int(c.foodQuantity)+int(request.POST['foodQuantity'])
							sqlupdate='UPDATE cart_tbl SET foodQuantity ={0} WHERE id={1}'.format(newQuantity,c.id)
							cursor.execute(sqlupdate)
							break
						else:
							print("in else save")
							form.save()
							return redirect('/foodapp/foods')

		else:
			print("Else")
			messages.info(request,"Please enter the value less than food Quantity"+str(food.quantity))
			return redirect('/foodapp/foods')
	return render(request,'cartapp/addcart.html',{'form':form})

def showCartView(request):
	email=request.session['email']
	cart=CartModel.objects.raw('SELECT c.id,f.name,f.price,c.foodQuantity from  cart_tbl as c INNER JOIN foodapp_foodmodel as f ON f.id=c.foodIdfk and c.emailIdfk = %s',[email])
	error="Your cart is Empty add food in cart"
	return render(request,"cartapp/cart.html",{'cart':cart,'error':error})

def deleteCartView(request,id):
	cart=CartModel.objects.get(id=id)
	cart.delete()
	return redirect('/cartapp/showcart')
