from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
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
    
    def __unicode__(self):
        return self.Name
    def get_absolute_url(self):
        return reverse("MY_MUSIC:detail",kwargs={"id":self.id})
