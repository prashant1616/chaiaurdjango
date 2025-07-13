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
    
class ChaiReview(models.Model):
        chai = models.ForeignKey(Chaivariety,on_delete= models.CASCADE,related_name='review')
        user = models.ForeignKey(User,on_delete=models.CASCADE)
        rating = models.IntegerField()
        comment = models.TextField()
        date_added = models.DateTimeField(default = timezone.now)
        def __str__(self):
             return f'{self.user.username} review for {self.chai.name}'


# Many to one


class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_variety = models.ManyToManyField(Chaivariety,related_name='stores')
    
    def __str__(self):
         return self.name
     
#one to one

class Chaicertification(models.model):
    chai = models.OneToOneField(Chaivariety,on_delete=models.CASCADE,related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date =models.DateTimeField(default=timezone.now)
    valid_until =models.DateTimeField()
    
    def __str__(self):
        return self.chai
    
    