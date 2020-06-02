from django.db import models

# Create your models here.
class FoodModel(models.Model):
	name=models.CharField(max_length=15);
	price=models.FloatField();
	quantity=models.IntegerField()

	def __str__(self):
		return "{0} {1} {2}".format(str(self.name),str(self.price),str(self.quantity))