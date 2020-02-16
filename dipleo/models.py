from django.db import models


class Users(models.Model):

    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    USER_TYPE = (
        ('Seeker', 'Seeker'),
        ('company', 'company'),
    )
    users_type = models.CharField(max_length=10, choices=USER_TYPE)
    objects = models.Manager()

    def __str__(self):
        return self.username