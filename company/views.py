from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Company, Users, Jobs, Job_Skill
from .serializers import UserSerializer, CompanySerializer, JobSerializer
from rest_framework.parsers import JSONParser
import json
from django.core import serializers

class CompanyList(APIView):
    def get(self, request):
        company_list = Company.objects.all()
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
        
        return Response(200)


class JobList(APIView):
    def get(self, request):
        job_list = Jobs.objects.all()
        serializer = JobSerializer(job_list, many=True)
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
        print(company_id)

        company = Company.objects.get(id=company_id)

        job = Jobs.objects.create(company=company,
                                         job_title=job_title, industry=industry,
                                         country=country, city=city, salary=salary,
                                         job_type=job_type, work_days=work_days, num_vacanices=num_vacanices,
                                         qualification=qualification, description=description,
                                         create_date=create_date, expiry_date=expiry_date,
                                         total_exp=total_exp)
       
        skills = json.loads(profile_data.get('skills'))
        for skill in skills:
            tech = skill.get('skill')
            exp = skill.get('exp')
            Job_Skill.objects.create(job=job, skill=tech, experience=exp)
        
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


        abc = Jobs.objects.filter(job_title=title, city=city, industry=industry, total_exp=total_exp, 
                            salary=salary, job_type=job_type)

        response = serializers.serialize('json', abc)

        #print(response)
        return Response(response, content_type='application/json')

