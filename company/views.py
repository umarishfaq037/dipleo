# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Company, Users, Jobs, Job_Skill
from user.models import ApplyJob, Settings
from .serializers import UserSerializer, CompanySerializer, JobSerializer
from rest_framework.parsers import JSONParser
from django.db.models import Q
import json
from django.core import serializers

class CompanyList(APIView):
    def get(self, request):
        company_data = request.query_params
        company_id = company_data.get('company_id')
        company_list = Company.objects.filter(id=company_id)
        serializer = CompanySerializer(company_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        profile_data = request.data
        name = profile_data.get('name')
        business_name = profile_data.get('business_name')
        nit = profile_data.get('nit')
        site_url = profile_data.get('site_url')
        sector = profile_data.get('sector')
        address = profile_data.get('address')
        city = profile_data.get('city')
        country = profile_data.get('country')
        total_emp = profile_data.get('total_emp')
        description = profile_data.get('description')
        doc_type = profile_data.get('doc_type')
        doc_num = profile_data.get('doc_num')
        creation_date = profile_data.get('creation_date')
        founder_name = profile_data.get('founder_name')
        founder_email = profile_data.get('founder_email')
        founder_phone = profile_data.get('founder_phone')
        founder_address = profile_data.get('founder_address')
        password = profile_data.get('password')
        email = profile_data.get('email')

        user = Users.objects.create(username=email, password=password, users_type='company')
        company_add = Company.objects.create(user=user,
                                         name=name, business_name=business_name,
                                         nit=nit, site_url=site_url, sector=sector,
                                         address=address, city=city, country=country, total_emp=total_emp,
                                         description=description, doc_type=doc_type, doc_num=doc_num,
                                         creation_date=creation_date, founder_name=founder_name, founder_email=founder_email,
                                         founder_phone=founder_phone, founder_address=founder_address)
        
        Settings.objects.create(user=user, user_status='looking_for_a_job')
        return Response(200)


class JobList(APIView):
    def get(self, request):
        user_data = request.query_params
        job_id = user_data.get('job_id')
        company_id = user_data.get('company_id')
        if job_id and company_id:
            job_profile = Jobs.objects.filter(id=job_id, company= company_id)
        elif job_id:
            job_profile = Jobs.objects.filter(id=job_id)
        elif company_id:
            job_profile = Jobs.objects.filter(company= company_id)
        else:
            job_profile = Jobs.objects.all()
        serializer = JobSerializer(job_profile, many=True)
        return Response(serializer.data)

    def post(self, request):
        profile_data = request.data
        job_title = profile_data.get('job_title')
        industry = profile_data.get('industry')
        city = profile_data.get('city')
        country = profile_data.get('country')
        salary = profile_data.get('salary')
        job_type = profile_data.get('job_type')
        work_days = profile_data.get('work_days')
        num_vacanices = profile_data.get('num_vacanices')
        qualification = profile_data.get('qualification')
        description = profile_data.get('description')
        create_date = profile_data.get('create_date')
        expiry_date = profile_data.get('expiry_date')
        total_exp = profile_data.get('total_exp')
        company_id = profile_data.get('company_id')

        company = Company.objects.get(id=company_id)

        job = Jobs.objects.create(company=company,
                                         job_title=job_title, industry=industry,
                                         country=country, city=city, salary=salary,
                                         job_type=job_type, work_days=work_days, num_vacanices=num_vacanices,
                                         qualification=qualification, description=description,
                                         create_date=create_date, expiry_date=expiry_date,
                                         total_exp=total_exp)
       
        skills = profile_data.get('skills')
        skills = json.loads(skills) if skills else []
        for skill in skills:
            tech = skill.get('skill')
            exp = skill.get('exp')
            Job_Skill.objects.create(job=job, skill=tech, experience=exp)
        
        return Response(200)


class CompanyJobs(APIView):
    def get(self, request):
        user_data = request.query_params
        company_id = user_data.get('company_id')
        job_profile = Jobs.objects.filter(company_id=company_id)
        serializer = JobSerializer(job_profile, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass

class CreateAppointment(APIView):

    def get(self, request):
        pass

    def post(self, request):
        user_data = request.data
        apply_job_id = user_data.get('apply_job_id')
        appointment_date = user_data.get('appointment_date')
        job_profile = ApplyJob.objects.filter(id=apply_job_id).update(appointment_date=appointment_date)
        if not job_profile:
            return Response(500)
        return Response(200)

class JobSearch(APIView):
    def get(self, request):
        job_list = Jobs.objects.all()
        serializer = JobSerializer(job_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        job_list = request.data
        title = job_list.get('job_title')
        city = job_list.get('city')
        industry = job_list.get('industry')
        total_exp = job_list.get('total_exp')
        salary = job_list.get('salary')
        job_type = job_list.get('job_type')

        query = Q()

        if title:
            query &= Q(job_title=title)
        if city:
            query &= Q(city=city)
        if industry:
            query &= Q(industry=industry)
        if total_exp:
            query &= Q(total_exp=total_exp)
        if salary:
            query &= Q(salary=salary)
        if job_type:
            query &= Q(job_type=job_type)

        jobs = Jobs.objects.filter(query)

        response = serializers.serialize('json', jobs)

        return Response(response, content_type='application/json')

