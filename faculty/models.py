from django.contrib.auth.models import User
from django.db import models
from administrator.models import Institute


# Create your models here.
class faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, null=False, blank=False)
    enroll_no = models.PositiveIntegerField(unique=True, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'faculties'

    def __str__(self):
        return f'faculty-{self.enroll_no}@{self.institute}-{self.email}'
