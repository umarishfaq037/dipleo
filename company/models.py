# -*- coding: utf-8 -*-
from django.db import models
from user.models import Users
from datetime import datetime

class Company(models.Model):
    user = models.OneToOneField(Users, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100, null=True)
    business_name = models.CharField(max_length=100, null=True)
    nit = models.CharField(max_length=40, null=True)
    site_url = models.CharField(max_length=30, null=True)
    sector = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    total_emp = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500, null=True)
    doc_type = models.CharField(max_length=50, null=True)
    doc_num = models.CharField(max_length=30, null=True)
    creation_date = models.DateField(default=datetime.now)
    founder_name = models.CharField(max_length=30, null=True)
    founder_email = models.CharField(max_length=30, null=True)
    founder_phone = models.CharField(max_length=30, null=True)
    founder_address = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.name

class Jobs(models.Model):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    job_title = models.CharField(max_length=30, null=True)
    industry = models.CharField(max_length=30, null=True)
    city = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=30, null=True)
    salary = models.IntegerField(default=1000, null=True)
    job_type = models.CharField(max_length=30, null=True)
    work_days = models.CharField(max_length=100, null=True)
    num_vacanices = models.IntegerField(default=1, null=True)
    qualification = models.CharField(max_length=30, null=True)
    description = models.TextField(max_length=500, null=True)
    create_date = models.DateField(default=datetime.now, blank=True, null=True)
    expiry_date = models.DateField(null=True)
    total_exp = models.IntegerField(default=1)

    def __str__(self):
        return self.job_title

class Job_Skill(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.DO_NOTHING, default=False)
    skill = models.CharField(max_length=50, null=True)
    experience = models.IntegerField(null=True)


class Applicants(models.Model):
    user = models.ForeignKey(Users, on_delete=models.DO_NOTHING)

class JobApplication(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.DO_NOTHING)
    applicant = models.ForeignKey(Applicants, on_delete=models.DO_NOTHING)
