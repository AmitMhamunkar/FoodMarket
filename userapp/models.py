from django.db import models

# Create your models here.

class UserModel(models.Model):
	#utypes=[('User','User'),('Admin','Admin')]
	#name=models.CharField(max_length=30,default='NA')
	#addr=models.CharField(max_length=30,default='NA')
	#contact=models.IntegerField(default=0)
	email=models.CharField(max_length=30)
	password=models.CharField(max_length=20)
	#utype = models.CharField(max_length=15,choices=utypes)
	def __str__(self):
		return "{0} {1}".format(self.email,self.password)

class AdminModel(models.Model):
	email=models.CharField(max_length=30)
	password=models.CharField(max_length=20)
	
	def __str__(self):
		return "{0} {1}".format(self.email,self.password)