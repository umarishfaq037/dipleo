from django.db import models
#from company.models import Jobs
class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    
    USER_TYPE = (
    ('Seeker', 'Seeker'),
    ('company', 'company'),
)
    users_type = models.CharField(max_length=10, choices=USER_TYPE)

    def __str__(self):
        return self.username

class Profile(models.Model):
    users = models.OneToOneField(Users, on_delete=models.DO_NOTHING)
    identification_type = models.CharField(max_length=60)
    identification_number = models.CharField(max_length=60)
    birth_date = models.DateField()
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
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
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    AVAILABLE = (
        ('move', 'move'),
        ('travel', 'travel')
    )
    #academy_id . It will be a foreign key
    password = models.CharField(max_length=50)
    years_of_experience = models.IntegerField()
    CURRENT_SITUATION = (
        ('working', 'working'),
        ('looking_for_job', 'looking_for_job')
    )
    best_attributes = models.CharField(max_length=255)
    interesting_data = models.TextField()
    activity1 = models.CharField(max_length=100)
    activity2 = models.CharField(max_length=100)
    licenses = models.BooleanField(default=False)
    vehicle = models.BooleanField(default=False)
    disabilities = models.BooleanField(default=False)
    industry1 = models.CharField(max_length=100)
    industry2 = models.CharField(max_length=100)
    industry3 = models.CharField(max_length=100)
    industry4 = models.CharField(max_length=100)
    industry5 = models.CharField(max_length=100)
    City1 = models.CharField(max_length=100)
    City2 = models.CharField(max_length=100)
    City3 = models.CharField(max_length=100)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField

class Education(models.Model):
    profiles = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    school = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    education_level = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    data_of_graduation = models.DateField

class Scholarship(models.Model):
    profiles = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    date = models.DateField()

class Employement(models.Model):
    profiles = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    company_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    achievements = models.CharField(max_length=255)

class Reference(models.Model):
    profiles = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class Skill(models.Model):
    profiles = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    value = models.IntegerField()

class Language(models.Model):
    profiles = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    value = models.IntegerField()

class Programming(models.Model):
    profiles = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    value = models.IntegerField()

class Design(models.Model):
    profiles = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    value = models.IntegerField()

class Data(models.Model):
    profiles = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    value = models.IntegerField()

class UserInterestedJobs(models.Model):
    profiles = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    job = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, related_name='job')
    is_interested = models.BooleanField()
    comment = models.TextField()