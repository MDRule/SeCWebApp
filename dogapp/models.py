from django.db import models
from django.contrib.auth.models import User  # Import User model

class Breed(models.Model):
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=20)
    friendliness = models.IntegerField()
    trainability = models.IntegerField()
    sheddingamount = models.IntegerField()
    exerciseneeds = models.IntegerField()

    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, default='Male')  # Add a default value
    color = models.CharField(max_length=50, default='Unknown')  # Add a default value
    favoritefood = models.CharField(max_length=255, default='Kibble')  # Add a default value
    favoritetoy = models.CharField(max_length=255, default='Ball')  # Add a default value
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Add owner field

    def __str__(self):
        return self.name
