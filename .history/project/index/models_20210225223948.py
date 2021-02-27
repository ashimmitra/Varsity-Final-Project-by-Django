from django.db import models

class AboutSite(models.Model):
    title=models.CharField(max_length=150,blank=False)
    description=models.TextField(max_length=800,blank=False)

    def__str__(self):
    return self.title    
