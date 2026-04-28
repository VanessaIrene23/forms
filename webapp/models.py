from django.db import models

# Create your models here.
class LineUp(models.Model):
    name = models.TextField() # Name: Vanessa
    position = models.TextField(max_length=10) # captain, ON, GK


class Contribution(models.Model):
    name = models.TextField()
    amount = models.IntegerField(default= 10, blank=False)
    phone = models.CharField(max_length=15)

class Task(models.Model):
    
    title = models.TextField(blank=False)
    description = models.CharField()
    priority = models.CharField(max_length=25)
    duedate = models.DateField() #2023-06-30
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=False)


