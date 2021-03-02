from __future__ import unicode_literals
from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # agregue claves y valores al diccionario de errores para cada campo no válido
        if len(postData['title']) < 5:
            errors["title"] = "El titulo debe tener al menos 5 caracteres"
        if len(postData['network']) < 3:
            errors["network"] = "El network debe tener al menos 3 caracteres"
#        if len(postData['release_date']) < 5:
#           errors["release_date"] = "Blog name should be at least 5 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "La descripcion debe tener al menos 10 caracteres"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

