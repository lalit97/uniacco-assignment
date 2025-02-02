from django.db import models
from django.contrib.auth.models import User 


class UserLoginHistory(models.Model):
    """
    Model to store User login records
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField(protocol='both')

    def __str__(self):
        return f'{self.user}'
