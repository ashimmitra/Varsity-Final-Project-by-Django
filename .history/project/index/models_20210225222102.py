from django.db import models

class AboutSite(models.Model):
    title=models.CharField(max_length=100,blank=False)
    description=models.CharField(max_length=500,blank=False)
