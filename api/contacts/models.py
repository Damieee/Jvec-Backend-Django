from django.db import models
from ..authentication.models import MyCustomUser


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        MyCustomUser,
        on_delete=models.CASCADE,
        related_name='my_custom_user_contacts',
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.phone_number}'
