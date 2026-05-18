from django.db import models

# Create your models here.
class user(models.Model):
    nume = models.CharField(max_length=30)
    prenume = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    parola = models.CharField(max_length=32)
    tip_persoana = models.CharField(max_length=10)
    companie = models.CharField(max_length=60, blank=True, null=True)
    adresa = models.CharField(max_length=150)
    status_cos = models.BooleanField()

    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.nume + " " + self.prenume