from django.db import models

# Create your models here.

class Item(models.Model):
    # Adding column/attribute
    text = models.TextField(default='')
