from django.db import models
from django.db.models import Model
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator


class Thing(Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=120, blank=True)
    quantity = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
     )