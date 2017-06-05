from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from location_field.models.plain import PlainLocationField
# Create your models here.
class UserProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Name=models.CharField(max_length=150,null=False,blank=False)
    Email=models.EmailField(null=False,blank=False)
    Telephone=models.IntegerField()
    content = models.TextField()
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    # location_2 = models.CharField(max_length=254)
    def __unicode__(self):
        return self.Name

class Category(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category_title=models.CharField(max_length=120)
    Name=models.CharField(max_length=120)
    Price=models.CharField(max_length=120)
    category_logo=models.ImageField(upload_to='photos/%Y/%m/%d/', null=True,blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __unicode__(self):
        return self.category_title
    
        
