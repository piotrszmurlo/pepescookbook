from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='recipes', on_delete=models.SET_NULL, null=True)
