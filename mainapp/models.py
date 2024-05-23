from django.db import models

# Create your models here.

class Departement(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Liste_Projet(models.Model):
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, related_name='liste_projet')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
