from django.db import models

from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.
class Phone(models.Model):

    number = PhoneNumberField()

    def __str__(self):
        return self.number.as_e164