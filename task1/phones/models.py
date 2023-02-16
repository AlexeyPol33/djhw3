from django.db import models


class Phone(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(max_length=100)
    price = models.FloatField(max_length=100)
    image = models.TextField(max_length=100)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField('URL',unique=True)

