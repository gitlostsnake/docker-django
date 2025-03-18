from django.contrib.auth.models import AbstractUser
from django.db import models

# custom user now has inherited everything from default django user model.
# we can now change this model and extend abstract user without profile models at a later date.
class CustomUser(AbstractUser):
    has_done = models.BooleanField(default=False)
