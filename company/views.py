from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Company, Users
from .serializers import UserSerializer, CompanySerializer
from rest_framework.parsers import JSONParser
import json

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
