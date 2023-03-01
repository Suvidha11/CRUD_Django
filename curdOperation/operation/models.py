from django.db import models

# Create your models here.
class student(models.Model):
    stu_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    branch=models.CharField(max_length=20)
    
