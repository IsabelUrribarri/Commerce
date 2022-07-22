from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionList(models.Model):
    active = models.BooleanField()
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    url_image = models.URLField(max_length=200,blank=True, null=True)
    description = models.TextField()



