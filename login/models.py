from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone =models.CharField(max_length=10, blank=True)
	created=models.DateTimeField(auto_now_add=True)
	modified=models.DateTimeField(auto_now=True)


	def _str_(self):
		return self.user.username