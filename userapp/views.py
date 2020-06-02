from django.shortcuts import render,redirect
from userapp.models import UserModel,AdminModel
from userapp.forms import Userform
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def restTestView(request):
	print(request.GET['email'])
	email=request.GET['email']
	users=UserModel.objects.filter(email=request.GET['email'])
	if users.count() !=0:
		return HttpResponse('Already Exist',content_type='text/plain')
	return HttpResponse("ok",content_type='text/plain')

def showAllUser(request):
	allusers=UserModel.objects.all()
	return render(request,'userapp/users.html',{'users':allusers})

def deleteUserById(request,id):
	user=UserModel.objects.get(id=id)
	user.delete()
	return redirect('/userapp/users/')

def createUserView(request):
	form=Userform()
	if request.method=='POST':
		form=Userform(request.POST)
		if form.is_valid():
			form.save()	
			return redirect('/userapp/users/')
	#return render(request,'userapp/adduser.html',{'form':form})
	return render(request,'userapp/register.html',{'form':form})

def updateUserById(request):
	e=request.session['email']
	user=UserModel.objects.get(email=e)
	form=Userform(instance=user)
	if request.method=='POST':
		form=Userform(request.POST,instance=user)
		if form.is_valid():
			form.save()
			return redirect('/userapp/users/')
	return render(request,'userapp/updateuser.html',{'form':form})	

def UserLogin(request):
	print('in login')
	form=Userform()
	if request.method=='POST':
		form=Userform(request.POST)
		print(request.POST['password'])
		if form.is_valid():
			email=request.POST['email']
			password=request.POST['password']
			userType=request.POST['utype']
			if userType == "admin" :
				admin=AdminModel.objects.raw('select * from userapp_AdminModel')
				for a in admin:
					if a.email==email and a.password==password:
						print("In Admin")
						request.session['email']=email
						request.session['utype']="admin"
						return redirect('/foodapp/foods')
			elif userType == "user":
				print("In user")
				allusers=UserModel.objects.raw('select * from userapp_UserModel')
				for u in allusers:
					#if u.email==email and u.password==password and u.utype==userType:
					if u.email==email and u.password==password:	
						request.session['email']=email
						request.session['utype']="user"
						print(request.session['utype'])
						return redirect('/foodapp/foods')
				return render(request,'userapp/userlogin.html',{'form':form,'error':'Bad credentials'})	
			else:
				return render(request,'userapp/userlogin.html',{'form':form,'error':'Bad credentials'})	
	return render(request,'userapp/userlogin.html',{'form':form})		

def Logout(request):
	request.session.clear()
	return redirect('/foodapp/foods')
	