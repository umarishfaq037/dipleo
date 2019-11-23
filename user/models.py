from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    
    USER_TYPE = (
    ("Seeker", "Seeker"),
    ("company", "company"),
)
    users_type = models.CharField(max_length=10, choices=USER_TYPE)

class Profile(models.Model):
    users = models.OneToOneField(Users, on_delete=models.DO_NOTHING)
    identification = models.CharField(max_length=60)
    birth_date = models.DateField()
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=20)
    USER_GENDER = (
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
    )
    gender = models.CharField(max_length=10, choices=USER_GENDER)
    email = models.EmailField(max_length=30)
    description = models.TextField(max_length=255)
    contact = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    AVAILABLE = (
        ('Move', 'Move'),
        ('Travel', 'Travel')
    )
    availability = models.CharField(max_length=15, choices=AVAILABLE)
    #academy_id . It will be a foreign key

