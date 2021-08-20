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

class Contact(models.Model):
    name=models.CharField(max_length=100,blank=False)
    email=models.EmailField(max_length=100,blank=False)
    subject=models.CharField(max_length=200,blank=False)
    message=models.TextField(max_length=800,blank=False)

    def __str__(self):
        return self.subject    

class Books(models.Model):
    title = models.CharField(max_length=50)
    image=models.ImageField(upload_to='static/img/',blank=False)
    pdf = models.FileField(upload_to='static/media')

    def __str__(self):
        return self.title            

class Notice(models.Model):
    title = models.CharField(max_length=50)
    image=models.ImageField(upload_to='static/img/',blank=False)
    description=models.TextField(max_length=800,blank=False)

    def __str__(self):
        return self.title 