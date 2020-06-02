from django.db import models

# Create your models here.

class OrderModel(models.Model):
	emailIdfk=models.EmailField()
	date=models.CharField(max_length=20)
	totalamt=models.IntegerField()
	def __str__(self):
		return "{0} {1} {2}".format(self.emailIdfk,self.date,self.totalamt)
	class Meta:
		db_table="order_tbl"