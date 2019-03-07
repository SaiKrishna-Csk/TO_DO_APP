from django.db import models
#import datetime
# Create your models here.
class List(models.Model):
    task = models.CharField(max_length=264,unique=True)
    #date = models.CharField(max_length=264,default='11/11/11')
    #time = models.CharField(max_length=264,default='12:12')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task
