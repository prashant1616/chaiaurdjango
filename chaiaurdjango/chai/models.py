from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User

# Create your models here.


class Chaivariety(models.Model):
    chai_type_choice = [
        ('ml','mashala'),
        ('gr','ginger'),
        ('kl','kiwi'),
        ('pl','plain'),
        ('el','elichi')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=chai_type_choice)
    description =  models.TextField(default='')
    
    
    def __str__(self):
        return self.name
    
    #one to many
    
    # class ChaiReview(models.Model):
    #     chai = models.    
    
    
    
    
    