from django.db import models
from django.contrib import admin
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    headImg = models.FileField(upload_to = './upload')
    def __unicode__(self):
        return self.username
    
    
admin.site.register(User)