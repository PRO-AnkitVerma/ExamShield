from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    institute = models.OneToOneField('Institute', on_delete=models.CASCADE)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name
