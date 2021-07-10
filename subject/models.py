from django.db import models
from faculty.models import faculty

# Create your models here.

class Subject(models.Model):
    code = models.IntegerField(help_text='Enter subject code', default=1)
    name = models.CharField(max_length=200, help_text='Enter subject name', default="subject")
    #faculty = models.ForeignKey(faculty, on_delete=models.CASCADE)


    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name
