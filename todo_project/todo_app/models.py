from django.db import models

# Create your models here.
class todoapp(models.Model):
    activity_name=models.CharField(max_length=250)
    priority=models.IntegerField()
    date1=models.DateField()
    def __str__(self):
       return self.activity_name