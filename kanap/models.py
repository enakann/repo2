from django.db import models


class mod1(models.Model):
	name=models.CharField(max_length=200)
	age=models.IntegerField()
	date=models.DateField()


	def __str__(self):
		return self.name


