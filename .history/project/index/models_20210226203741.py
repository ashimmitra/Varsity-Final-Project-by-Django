from django.db import models

class AboutSite(models.Model):
    title=models.CharField(max_length=150,blank=False)
    description=models.TextField(max_length=800,blank=False)

    def __str__(self):
        return self.title    

class Slider(models.Model):
    title=models.CharField(max_length=150,blank=False)
    description=models.TextField(max_length=800,blank=False)
    image=models.ImageField(upload_to='slider/',blank=False)

    def __str__(self):
        return self.title

class AboutSite(models.Model):
    title=models.CharField(max_length=150,blank=False)
    description=models.TextField(max_length=800,blank=False)

    def __str__(self):
        return self.title        