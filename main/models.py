from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Shopping_item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    bought = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name
