# groups/models.py
from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    currentWallpaper = models.CharField(max_length=255, blank=True, null=True)
    # Adicione outros campos conforme necessário
