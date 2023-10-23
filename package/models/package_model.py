from django.core.validators import MinValueValidator
from django.db import models


class Package(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    price = models.FloatField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name
