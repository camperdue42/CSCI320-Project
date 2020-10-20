from django.db import models

# Create your models here.
class user(models.Model):
	u_uid = models.IntegerField()
	u_name = models.CharField(max_length=100)
