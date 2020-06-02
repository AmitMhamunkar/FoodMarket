from django.shortcuts import render,redirect
from orderapp.models import OrderModel
from orderapp.forms  import OrderForm
import datetime
from django.db import connection
from cartapp.models import CartModel
from foodapp.models import FoodModel
# Create your views here.

def showOrderView(request):
	email=request.session['email']
	order=OrderModel.objects.filter(emailIdfk=email)
	return render(request,'orderapp/order.html',{'order':order})

def clearOrder(request):
	OrderModel.objects.filter(emailIdfk=email).delete()
	

def placeOrderView(request):
	form=OrderForm()
	if request.method == 'POST':
		orderDate=datetime.date.today()
		email=request.session['email']
		cursor=connection.cursor()
		total=cursor.execute("select sum(f.price * c.foodQuantity) from foodapp_foodmodel as f inner join cart_tbl as c on f.id=c.foodIdfk and c.emailIdfk=%s",[email])
		totalbill=float(cursor.fetchone()[0])
		insertsql='INSERT INTO order_tbl(totalamt,date,emailIdfk)values("%f","%s","%s")'%(totalbill,orderDate,email)
		cursor.execute(insertsql)
		cart=CartModel.objects.all()
		food=FoodModel.objects.all()
		for c in cart:
			for f in food:
				if int(c.foodIdfk)==int(f.id):
					newQuantity=int(f.quantity)-int(c.foodQuantity)
					print(newQuantity)
					sqlupdate='UPDATE foodapp_foodmodel SET quantity ={0} WHERE id={1}'.format(newQuantity,f.id)
					cursor.execute(sqlupdate)
		#CartModel.objects.filter(emailIdfk=email).delete()
		#return redirect('/foodapp/foods')
		return render(request,'orderapp/bill.html')
		CartModel.objects.filter(emailIdfk=email).delete()
	return render(request,'cartapp/order.html',{'form':form})