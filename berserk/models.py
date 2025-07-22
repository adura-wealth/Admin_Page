from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=2)
    content = models.TextField()
    
    
    class Beta:
        db_table ="post"
        
class Invoice(models.Model):
    price = models.IntegerField(max_length=2)
    desciption = models.TextField()
    
    
    class Beta:
        db_table ="invoice"