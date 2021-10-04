from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=30)
    population = models.PositiveIntegerField()

    

        
        
class State(models.Model):
    name = models.CharField(max_length=30)
    population = models.PositiveIntegerField()
        
        
        
        

class City(models.Model):
    city_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    population = models.PositiveIntegerField()
    
    
    
        
    
    
    
    