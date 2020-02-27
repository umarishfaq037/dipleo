from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from company.models import *
from .serializers import UserSerializer, UserProfileSerializer, SaveJobsSerializer
from rest_framework.parsers import JSONParser
import json

class Login(APIView):
    def get(self, request):
        user = Profile.objects(users_id=32).update(users_id=1)
        return Response(user.users_id)


    def post(self, request):
        try:
            profile_data = request.data
            email = profile_data.get('email')
            password = profile_data.get('password')
            users_type = profile_data.get('type')
            user = Users.objects.get(username=email, password=password, users_type=users_type)
            content = {}
            if user:
                content = {"username": user.username, "type": user.users_type, "user_id": user.id, "status": 200}
            else:
                content = {"error": "Wrong Email or Password"}
        except Exception as e:
            print(str(e))
            content = {"error": "Wrong Email or Password"}

        return Response(content)


class UsersList(APIView):
    def get(self, request):
        users_list = Users.objects.all()
        serializer = UserSerializer(users_list, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class UserProfile(APIView):
    def get(self, request):
        user_profile_list = Profile.objects.all()
        serializer = UserProfileSerializer(user_profile_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        profile_data = request.data
        identification_type = profile_data.get('identification_type')
        identification_number = profile_data.get('identification_number')
        birth_date = profile_data.get('birth_date')
        name = profile_data.get('name')
        surname = profile_data.get('surname')
        gender = profile_data.get('gender')
        email = profile_data.get('email')
        description = profile_data.get('description')
        contact = profile_data.get('contact')
        address = profile_data.get('address')
        city = profile_data.get('city')
        country = profile_data.get('country')
        available = profile_data.get('available')
        password = profile_data.get('password')
        years_of_experience = profile_data.get('years_of_experience')
        current_situation = profile_data.get('current_situation')
        best_attributes = profile_data.get('best_attributes')
        interesting_data = profile_data.get('interesting_data')
        activity1 = profile_data.get('activity1')
        activity2 = profile_data.get('activity2')

        licenses = profile_data.get('licenses')
        vehicle = profile_data.get('vehicle')
        disabilities = profile_data.get('disabilities')
        industry1 = profile_data.get('industry1')
        industry2 = profile_data.get('industry2')
        industry3 = profile_data.get('industry3')
        industry4 = profile_data.get('industry4')
        industry5 = profile_data.get('industry5')

        city1 = profile_data.get('city1')
        city2 = profile_data.get('city2')
        city3 = profile_data.get('city3')
        min_salary = profile_data.get('min_salary')
        max_salary = profile_data.get('max_salary')

        user = Users.objects.create(username=email, password=password, users_type='Seeker')
        profile = Profile.objects.create(users=user,
                                         identification_type=identification_type,
                                         identification_number=identification_number, birth_date=birth_date,
                                         name=name, surname=surname, gender=gender, email=email,
                                         description=description, contact=contact, address=address, city=city,
                                         country=country, available=available, years_of_experience=years_of_experience,
                                         current_situation=current_situation, best_attributes=best_attributes,
                                         interesting_data=interesting_data, activity1=activity1, activity2=activity2,
                                         licenses=licenses, vehicle=vehicle, disabilities=disabilities,
                                         industry1=industry1, industry2=industry2, industry3=industry3,
                                         industry4=industry4, industry5=industry5, city1=city1, city2=city2,
                                         city3=city3, min_salary=min_salary, max_salary=max_salary)

        #Educations
        educations = json.loads(profile_data.get('educations'))
        for education in educations:
            school = education.get('school')
            city = education.get('city')
            education_level = education.get('education_level')
            title = education.get('title')
            date_of_graduation = education.get('date_of_graduation')
            Education.objects.create(profiles=profile, school=school, city=city, education_level=education_level,
                                     title=title, date_of_graduation=date_of_graduation)
        # Scholarships
        scholarships = json.loads(profile_data.get('scholarships'))
        for scholarship in scholarships:
            name = scholarship.get('name')
            date = scholarship.get('date')

            Scholarship.objects.create(profiles=profile, name=name, date=date)

        # Employments
        employments = json.loads(profile_data.get('employments'))
        for employment in employments:
            company_name = employment.get('company_name')
            city = employment.get('city')
            from_date = employment.get('from_date')
            to_date = employment.get('to_date')
            achievements = employment.get('achievements')

            Employement.objects.create(profiles=profile, company_name=company_name, city=city, from_date=from_date,
                                       to_date=to_date, achievements=achievements)


        # References
        references = json.loads(profile_data.get('references'))
        for reference in references:
            first_name = reference.get('first_name')
            relationship = reference.get('relationship')
            phone = reference.get('phone')
            email = reference.get('email')

            Reference.objects.create(profiles=profile, first_name=first_name, relationship=relationship,
                                       phone=phone, email=email)

        # Skills
        skills = json.loads(profile_data.get('skills'))
        for skill in skills:
            name = skill.get('name')
            value = skill.get('value')

            Skill.objects.create(profiles=profile, name=name, value=value)

        # Language
        languages = json.loads(profile_data.get('languages'))
        for language in languages:
            name = language.get('name')
            value = language.get('value')

            Language.objects.create(profiles=profile, name=name, value=value)

        # Programming
        programmings = json.loads(profile_data.get('programmings'))
        for programming in programmings:
            name = programming.get('name')
            value = programming.get('value')

            Programming.objects.create(profiles=profile, name=name, value=value)

        # Design
        designs = json.loads(profile_data.get('designs'))
        for design in designs:
            name = design.get('name')
            value = design.get('value')

            Design.objects.create(profiles=profile, name=name, value=value)

        # Data
        datas = json.loads(profile_data.get('datas'))
        for data in datas:
            name = data.get('name')
            value = data.get('value')

            Data.objects.create(profiles=profile, name=name, value=value)
        return Response(200)

class ApplyJobs(APIView):
    def get(self, request):
        user_data = request.data
        user_id = user_data.get('user_id')
        all_applied_jobs = ApplyJob.objects.filter(user_id=user_id)
        # serializer = JobSerializer(job_list, many=True)
        return Response(all_applied_jobs)

    def post(self, request):
        user_data = request.data
        user_id = user_data.get('user_id')
        job_id = user_data.get('job_id')
        comment = user_data.get('comment')
        user = Users.objects.filter(id=user_id)
        job = Jobs.objects.filter(id=job_id)
        ApplyJob.objects.create(user=user[0], job=job[0], comment=comment)
        return Response(200)


class SavedJobs(APIView):
    def get(self, request):
        user_data = request.query_params
        user_id = user_data.get('user_id')
        all_applied_jobs = SavedJob.objects.filter(user_id=user_id)
        serializer = SaveJobsSerializer(all_applied_jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        user_data = request.data
        user_id = user_data.get('user_id')
        job_id = user_data.get('job_id')
        user = Users.objects.filter(id=user_id)
        job = Jobs.objects.filter(id=job_id)
        SavedJob.objects.create(user=user[0], job=job[0])
        return Response(200)