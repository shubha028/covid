from django.db import models

# Create your models here.


class Listing(models.Model):
    business_name = models.CharField(max_length=80)
    business_email = models.EmailField()
    business_website = models.CharField(max_length=80)
    business_phone = models.CharField(max_length=80)
