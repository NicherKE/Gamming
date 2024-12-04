from django.db import models

# Create your models here.
class Detail(models.Model):
    
    name=models.CharField(max_length=30)
    mail=models.CharField(max_length=30)
    passw=models.CharField(max_length=20)
    rpass=models.CharField(max_length=20)

class game(models.Model):

    link=models.CharField(max_length=30)
    gamename=models.CharField(max_length=40)
    description=models.TextField(max_length=1000)
    rating=models.IntegerField()
    link1=models.CharField(max_length=20)
   

    