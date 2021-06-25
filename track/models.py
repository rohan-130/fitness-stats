from django.db import models

class Exercises(models.Model):
	exercise_name = models.CharField(max_length=100, null=True) 
	exercise_time = models.CharField(max_length=100, null=True)
	creator_id = models.IntegerField(null=True)
	mon = models.CharField(max_length=5, null=True)
	tue = models.CharField(max_length=5, null=True)
	wed = models.CharField(max_length=5, null=True)
	thu = models.CharField(max_length=5, null=True)
	fri = models.CharField(max_length=5, null=True)
	sat = models.CharField(max_length=5, null=True)
	sun = models.CharField(max_length=5, null=True)

	def __str__(self):
		return self.exercise_name

class Day(models.Model):
	user_id = models.IntegerField()
	today = models.DateField() 
	exercise_id = models.IntegerField(null=True)

