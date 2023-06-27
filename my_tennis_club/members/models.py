from django.db import models

# Create your models here.

class Registerform(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    contact=models.CharField(max_length=50)
    email=models.EmailField()
    
    
    class Meta:
        db_table='datas'
    
    
# time=models.CharField(max_length=30)    