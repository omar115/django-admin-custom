from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    inventory = models.IntegerField()

    # return the object name, by using the
    # string representation of an object name in python
    # we use __str__ method
    def __str__(self) -> str:
        return self.title
    
    # how to change the ordering of objects?
    # we will Meta class to order the objects
    class Meta:
        ordering = ['title']
