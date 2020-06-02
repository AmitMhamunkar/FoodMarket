from django.db import models

# Create your models here.

class CartModel(models.Model):
	foodIdfk=models.IntegerField()
	foodQuantity=models.IntegerField()
	emailIdfk=models.EmailField()
	class Meta:
		db_table="cart_tbl"