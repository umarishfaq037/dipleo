from django.db import models
from user.models import Users

class CompanyProfile(models.Model):
    users = models.OneToOneField(Users, on_delete=models.DO_NOTHING)
    company_name = models.CharField(max_length=100)
    company_type = models.CharField(max_field=100)

class Jobs(models.Model):
    company = models.OneToOneField(CompanyProfile, on_delete=models.DO_NOTHING)
    job_title = models.TextField()
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    qualification = models.TextField()
    description = models.TextField()
    expiry = models.TextField()

class Applicants(models.Model):
    users = models.OneToManyField(Users, on_delete=models.DO_NOTHING)
    jobs = models.OneToManyField(Jobs, on_delete=models.DO_NOTHING)
