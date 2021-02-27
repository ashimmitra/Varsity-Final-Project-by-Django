from django.db import models

class AboutSite(models.Model):
    title=models.CharField(max_length=100,blank=False)
    description(group)=models.CharField(max_length=100,blank=False)
