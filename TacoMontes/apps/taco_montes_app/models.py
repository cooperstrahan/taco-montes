from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) < 2 or len(postData['name']) >255:
            errors['name'] = 'Your name is required.'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email_invalid'] = 'The email you entered is not valid.'
        if len(postData['email']) < 6 or len(postData['email']) > 255:
            errors['email'] = 'Your email is required.'
        return errors

class User(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length=255)
    document = models.FileField(upload_to='resume/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()