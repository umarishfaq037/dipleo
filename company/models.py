from django.db import models
from user.models import Users

class Company(models.Model):
    user = models.OneToOneField(Users, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Jobs(models.Model):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    job_title = models.CharField(max_length=30)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    qualification = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    expiry = models.DateField()

    def __str__(self):
        return self.job_title

class Applicants(models.Model):
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING)

class JobApplication(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.DO_NOTHING)
    applicant = models.ForeignKey(Applicants, on_delete=models.DO_NOTHING)
