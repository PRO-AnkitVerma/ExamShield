from django.contrib.auth.models import User
from django.db import models

class student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    institute = models.OneToOneField('Institute', on_delete=models.CASCADE)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
