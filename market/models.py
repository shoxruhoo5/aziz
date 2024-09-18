from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='users/', default='user_png')
    STATUS = ( 
        ('admin', 'Admin'), 
        ('user', 'User')      
    ) 
    phone = models.CharField(max_length=14,null=True, blank=True) 
    status = models.CharField(max_length=50, choices=STATUS, default='User')

 
    

