from pyexpat import model
from django.db import models

# Create your models here.

class Api(models.Model):
    base_route = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)