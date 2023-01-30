from django.db import models
from django.core.exceptions import ValidationError
def validateLengthGreaterThanTwo(value):
    if len(value) < 3:
        raise ValidationError(
            '{} must be longer than: 2'.format(value)
        )
# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=45, validators = [validateLengthGreaterThanTwo])
    lname = models.CharField(max_length=45,validators = [validateLengthGreaterThanTwo])
    email = models.CharField(max_length=45,validators = [validateLengthGreaterThanTwo])
    password = models.CharField(max_length=45,validators = [validateLengthGreaterThanTwo])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
