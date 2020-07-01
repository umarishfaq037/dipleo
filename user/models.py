from django.db import models
# from company.models import Jobs


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

class Profile(models.Model):
    user = models.OneToOneField(Users, on_delete=models.DO_NOTHING)
    identification_type = models.CharField(max_length=60, null=True)
    identification_number = models.CharField(max_length=60, null=True)
    birth_date = models.DateField(null=True)
    name = models.CharField(max_length=40, null=True)
    surname = models.CharField(max_length=40, null=True)
    USER_GENDER = (
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
    )
    gender = models.CharField(max_length=10, choices=USER_GENDER)
    email = models.EmailField(max_length=30, null=True)
    description = models.TextField(max_length=255, null=True)
    contact = models.CharField(max_length=25, null=True)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=30, null=True)
    AVAILABLE = (
        ('move', 'move'),
        ('travel', 'travel')
    )
    available = models.CharField(max_length=10, default='travel', choices=AVAILABLE)
    #academy_id . It will be a foreign key
    # password = models.CharField(max_length=50)
    years_of_experience = models.CharField(max_length=50, null=True)
    CURRENT_SITUATION = (
        ('working', 'working'),
        ('looking_for_job', 'looking_for_job')
    )
    current_situation = models.CharField(max_length=20, default='working', choices=CURRENT_SITUATION)
    best_attributes = models.CharField(max_length=255, null=True)
    interesting_data = models.TextField(null=True)
    activity1 = models.CharField(max_length=100, null=True)
    activity2 = models.CharField(max_length=100, null=True)
    licenses = models.BooleanField(default=False, null=True)
    vehicle = models.BooleanField(default=False, null=True)
    disabilities = models.BooleanField(default=False, null=True)
    industry1 = models.CharField(max_length=100, null=True)
    industry2 = models.CharField(max_length=100, null=True)
    industry3 = models.CharField(max_length=100, null=True)
    industry4 = models.CharField(max_length=100, null=True)
    industry5 = models.CharField(max_length=100, null=True)
    city1 = models.CharField(max_length=100, null=True)
    city2 = models.CharField(max_length=100, null=True)
    city3 = models.CharField(max_length=100, null=True)
    min_salary = models.IntegerField(null=True)
    max_salary = models.IntegerField(null=True)
    objects = models.Manager()

    def __str__(self):
        return self.name



class Education(models.Model):
    profiles = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    school = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    education_level = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    date_of_graduation = models.DateField(default=None, null=True)


class Scholarship(models.Model):
    profiles = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100, null=True)
    date = models.DateField(null=True)


class Employement(models.Model):
    profiles = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    company_name = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    achievements = models.CharField(max_length=255, null=True)


class Reference(models.Model):
    profiles = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=100, null=True)
    relationship = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)

class Skill(models.Model):
    profiles = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100, null=True)
    value = models.IntegerField(null=True)

class Language(models.Model):
    profiles = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100, null=True)
    value = models.IntegerField(null=True)

class Programming(models.Model):
    profiles = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100, null=True)
    value = models.IntegerField(null=True)

class Design(models.Model):
    profiles = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100, null=True)
    value = models.IntegerField(null=True)

class Data(models.Model):
    profiles = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100, null=True)
    value = models.IntegerField(null=True)


# class UserInterestedJobs(models.Model):
#     profiles = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
#     job = models.ForeignKey(Jobs, on_delete=models.DO_NOTHING, related_name='job')
#     is_interested = models.BooleanField()
#     comment = models.TextField()


class SavedJob(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    job = models.ForeignKey('company.Jobs', on_delete=models.DO_NOTHING)


class ApplyJob(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    job = models.ForeignKey('company.Jobs', on_delete=models.CASCADE)
    company = models.ForeignKey('company.Company', null = True, on_delete=models.CASCADE)
    comment = models.TextField()
    is_seen = models.BooleanField(default=False)
    is_evaluation = models.BooleanField(default=False)
    is_interview = models.BooleanField(default=False)
    is_offer = models.BooleanField(default=False)
    appointment_date = models.TextField(default=None, null=True)

    def __str__(self):
        return self.job


class SavedApplyJob(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    apply_job = models.ForeignKey(ApplyJob, on_delete=models.CASCADE)

    def __str__(self):
        return self.apply_job


class CandidateIntro(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    video_link = models.CharField(max_length=200)
    question = models.CharField(max_length=300)


class Notifications(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    notification = models.TextField()
    is_read = models.BooleanField(default=False)

class Subscribe(models.Model):
    email = models.TextField()

class Settings(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    vacany_suggestions = models.BooleanField(default=False, null=True)
    application_status = models.BooleanField(default=False, null=True)
    newsletter_promotions = models.BooleanField(default=False, null=True)
    USER_STATUS = (
        ('looking_for_a_job', 'Looking for a job'),
        ('open_to_opportunities', 'Open to opportunities'),
        ('inactive', 'inactive'),
    )
    user_status = models.CharField(max_length=30, choices=USER_STATUS)
    user_picture = models.TextField(null=True)
