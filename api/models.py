from django.db import models

# Create your models here.
class Skills(models.Model): 
    name = models.CharField(max_length=100,blank=True,null=True)
    experience_lvl = models.CharField(max_length=50,null=True,blank=True)



class Experience(models.Model):
    designation = models.TextField(blank=True,null=True)
    technology = models.TextField(blank=True,null=True)
    company = models.TextField(blank=True,null=True)
    startDate = models.TextField(blank=True,null=True)
    endDate = models.TextField(blank=True,null=True)