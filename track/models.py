from django.db import models

class UserLog(models.Model):
	user_id = models.IntegerField()
	plan_name = models.CharField(max_length=100)
	jan_score = models.IntegerField()
	feb_score = models.IntegerField()
	mar_score = models.IntegerField()
	apr_score = models.IntegerField()
	may_score = models.IntegerField()
	jun_score = models.IntegerField()
	jul_score = models.IntegerField()
	aug_score = models.IntegerField()
	sep_score = models.IntegerField()
	oct_score = models.IntegerField()
	nov_score = models.IntegerField()
	dec_score = models.IntegerField()
	week_score = models.IntegerField()
	def __str__(self):
		return self.plan_name

class Exercises(models.Model):
	creator_id = models.IntegerField()
	exercise_name = models.CharField(max_length=100)
	exercise_unit = models.CharField(max_length=100)
	def __str__(self):
		return self.exercise_name

class Plans(models.Model):
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
