from django.db import models

# Create your models here.
class Employee(models.Model):

	empid = models.CharField(max_length=40)
	empname = models.CharField(max_length=200)
	empemail = models.EmailField()
	empcontact = models.CharField(max_length=20)
	# class Meta():
	# 	db_table = "Employees"

	def __str__(self):
		return self.empname
