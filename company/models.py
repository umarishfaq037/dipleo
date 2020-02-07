from django.db import models
from user.models import Users
from datetime import datetime

class Company(models.Model):
    user = models.OneToOneField(Users, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100, default=False)
    business_name = models.CharField(max_length=100, default=False)
    nit = models.CharField(max_length=40, default=False)
    site_url = models.CharField(max_length=30, default=False)
    sector = models.CharField(max_length=50, default=False)
    address = models.CharField(max_length=100, default=False)
    city = models.CharField(max_length=50, default=False)
    country = models.CharField(max_length=50, default=False)
    total_emp = models.IntegerField(default=1)
    description = models.TextField(max_length=500, default=False)
    doc_type = models.CharField(max_length=50, default=False)
    doc_num = models.CharField(max_length=30, default=False)
    creation_date = models.DateField(default=datetime.now)
    founder_name = models.CharField(max_length=30, default=False)
    founder_email = models.CharField(max_length=30, default=False)
    founder_phone = models.CharField(max_length=30, default=False)
    founder_address = models.CharField(max_length=100, default=False)


    def __str__(self):
        return self.name

class Jobs(models.Model):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    job_title = models.CharField(max_length=30, default='Job Title')
    industry = models.CharField(max_length=30, default='industry')
    city = models.CharField(max_length=30, default='City')
    country = models.CharField(max_length=30, default='Country')
    salary = models.IntegerField(default=1000)
    job_type = models.CharField(max_length=30, default='Job Type')
    work_days = models.CharField(max_length=100, default='Work_days')
    num_vacanices = models.IntegerField(default=1)
    qualification = models.CharField(max_length=30, default='Qualification')
    description = models.TextField(max_length=500, default='Description')
    create_date = models.DateField(default=datetime.now)
    expiry_date = models.DateField()
    total_exp = models.IntegerField(default=1)

    def __str__(self):
        return self.job_title

class Job_Skill(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.DO_NOTHING, default=False)
    skill = models.CharField(max_length=50)
    experience = models.IntegerField()

class Applicants(models.Model):
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING)

class JobApplication(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.DO_NOTHING)
    applicant = models.ForeignKey(Applicants, on_delete=models.DO_NOTHING)
