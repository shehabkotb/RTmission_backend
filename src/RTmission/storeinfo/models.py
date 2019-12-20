from django.core.validators import RegexValidator
from django.db import models

class UserInfo(models.Model):
    # name length limited to 100 chars
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=11, validators=[
        RegexValidator(
            regex=r'^01\d{9}$', 
            message="please enter 11 digits in form '01xxxxxxx'"
            )
        ]) 
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    comment = models.CharField(max_length=256, blank=True, null=True)

