from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    Male = "Male"
    Female = "Female"
    gender_choices = [
        (Male,'Male'),
        (Female,'Female')
    ]
    gender= models.CharField(
        max_length=20,
        choices=gender_choices,
        default=Female,
    )
    symptoms = models.CharField(max_length=80)
    prescription = models.CharField(max_length=80)
    date_of_visit = models.DateField()
    def __str__(self):
        return self.name
