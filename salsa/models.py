from django.db import models

class Recipes(models.Model):
    title = models.CharField(max_length=255)