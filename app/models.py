from django.db import models

# Create your models here.
class Population(models.Model):
    Country = models.CharField(max_length=100)
    Year = models.IntegerField()
    Human_count = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.Country} => {self.Human_count}"