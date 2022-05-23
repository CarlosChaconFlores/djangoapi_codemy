from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    price = models.FloatField(max_length=10)

    #Change the object representation to a string
    def __str__(self):
        return self.name