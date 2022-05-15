from django.db import models
from django.urls import reverse

# Create your models here.
class Caretaker(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('caretakers_detail', kwargs={'pk': self.id})

class Plant(models.Model):  # Note that parens are optional if not inheriting from another class
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    age = models.IntegerField()
    caretakers = models.ManyToManyField(Caretaker)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})

class Watering(models.Model):
    date = models.DateField('watering date')

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"Watered on {self.date}"
    
    class Meta:
        ordering = ['-date']

