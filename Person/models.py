from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser



def cinValidation(cin):
    if len(str(cin))!=8:
        raise ValidationError('Cin must be 8 characters!!')
    return cin
    

# Create your models here.
class Person(AbstractUser):
    cin=models.IntegerField(primary_key=True,validators=[cinValidation])
    email=models.EmailField(unique=True)