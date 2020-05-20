from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from company.models import *
from user.password_generator import PasswordResetTokenGenerator
from user.generate_email import *
from .serializers import *
from rest_framework.parsers import JSONParser
import json
from django.db.models import Count
from django.http import HttpResponse



class Login(APIView):
    def get(self, request):
        # user = Profile.objects(users_id=32).update(users_id=1)
        # return Response(user.users_id)
        pass

    def post(self, request):
        try:
            profile_data = request.data
            email = profile_data.get('email')
            password = profile_data.get('password')
            # users_type = profile_data.get('type')
            user = Users.objects.get(username=email, password=password)
            if user:
                if user.users_type == 'Seeker':
                    profile = Profile.objects.get(user=user)
                    content = {"username": user.username, "type": user.users_type, "user_id": user.id, "firstname": profile.name, "surname": profile.surname, "status": 200}
                else:
                    profile = Company.objects.get(user=user)
                    content = {"username": user.username, "type": user.users_type, "user_id": user.id, "founder_name": profile.founder_name, "company_id": profile.id, "company_name": profile.name, "status": 200}
            else:
                content = {"error": "Wrong Email or Password"}
        except Exception as e:
            print(str(e))
            content = {"error": "Error"}
        return Response(content)

class ForgetPassword(APIView):
    def get(self, request):
        user_data = request.query_params
        token = user_data.get('token')
        email = user_data.get('user')
        user = Users.objects.filter(username=email)
        default_token_generator = PasswordResetTokenGenerator()
        if user:
            check = default_token_generator.check_token({"pk": user[0].id, "username": user[0].username,
                                                            "password": user[0].password}, token)
            if check:
                return Response(200)
        return Response(404)


    def post(self, request):
        user_data = request.data
        email = user_data.get('email')
        user = Users.objects.filter(username=email)
        if user:
            default_token_generator = PasswordResetTokenGenerator()
            token = default_token_generator.make_token({"pk": user[0].id, "username": user[0].username,
                                                        "password": user[0].password})
            send_email(user[0].username, "http://dipleo.com:8000/forget_password?user={}&token={}".format(user[0].username,
                                                                                                          token))
            # print(token)
            return Response(200)

        return Response(404)

    def put(self, request):
        user_data = request.data
        token = user_data.get('token')
        email = user_data.get('user')
        password = user_data.get('password')
        print(email)
        user = Users.objects.filter(username=email)
        default_token_generator = PasswordResetTokenGenerator()
        if user:
            check = default_token_generator.check_token({"pk": user[0].id, "username": user[0].username,
                                                         "password": user[0].password}, token)
            if check:
                Users.objects.filter(username=email).update(password=password)
                return Response(200)
        return Response(404)

class UsersList(APIView):
    def get(self, request):
        users_list = Users.objects.all()
        serializer = UserSerializer(users_list, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class UserProfile(APIView):
    def get(self, request):
        user_data = request.query_params
        user_id = user_data.get('id')
        if not user_id:
            user_profile = Profile.objects.all()
            serializer = UserProfileSerializer(user_profile, many=True)
            return Response(serializer.data)
        
        else:
            user = Users.objects.get(id=user_id)
            user_profile = Profile.objects.filter(user=user)
            user_profile2 = Profile.objects.get(user=user)

            education = Education.objects.filter(profiles=user_profile2)
            programming = Programming.objects.filter(profiles=user_profile2)
            skills = Skill.objects.filter(profiles=user_profile2)
            data_ser = Data.objects.filter(profiles=user_profile2)
            scholarship = Scholarship.objects.filter(profiles=user_profile2)
            design = Design.objects.filter(profiles=user_profile2)
            reference = Reference.objects.filter(profiles=user_profile2)
            lang = Language.objects.filter(profiles=user_profile2)
            intro = Employement.objects.filter(profiles=user_profile2)

            serializer = UserProfileSerializer(user_profile, many=True)
            serializer2 = EducationSerializer(education, many=True)
            serializer3 = ProgrammingSerializer(programming, many=True)
            serializer4 = SkillSerializer(skills, many=True)
            serializer5 = DataSerializer(data_ser, many=True)
            serializer6 = ScholarshipSerializer(scholarship, many=True)
            serializer7 = DesignSerializer(design, many=True)
            serializer8 = ReferenceSerializer(reference, many=True)
            serializer9 = LanguageSerializer(lang, many=True)
            serializer10 = EmploymentSerializer(intro, many=True)

            return Response(serializer.data + serializer2.data + serializer3.data +
                            serializer4.data + serializer5.data + serializer6.data +
                            serializer7.data + serializer8.data + serializer9.data + serializer10.data)

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

        profile = Profile.objects.create(user=user,
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

        Settings.objects.create(user=user, user_status='looking_for_a_job')
        return Response(200)

class ApplyJobs(APIView):
    def get(self, request):
        user_data = request.query_params
        user_id = user_data.get('user_id')
        company_id = user_data.get('company_id')
        if user_id:
            profile = Profile.objects.get(user_id = user_id)
            all_applied_jobs = ApplyJob.objects.filter(user=profile)
        elif company_id:
            all_applied_jobs = ApplyJob.objects.filter(company_id=company_id)   
        else:
            all_applied_jobs = ApplyJob.objects.all()
        serializer = ApplyJobsSerializer(all_applied_jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        user_data = request.data
        user_id = user_data.get('user_id')
        user = Users.objects.get(id = user_id)
        profile = Profile.objects.filter(user_id=user_id)
        job_id = user_data.get('job_id')
        comment = user_data.get('comment')
        user = Users.objects.filter(id=user_id)
        job = Jobs.objects.get(id=job_id)
        company = job.company
        ApplyJob.objects.create(user= profile[0], job=job, comment=comment, company= company)
        return Response(200)


class CandidateApplyJobs(APIView):
    def get(self, request):
        user_data = request.query_params
        all_candidates_applied_jobs = ApplyJob.objects.all()
        serializer = CandidateApplyJobsSerializer(all_candidates_applied_jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass

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


class SavedApplyJobss(APIView):
    def get(self, request):
        all_saved_jobs = SavedApplyJob.objects.all()
        serializer = SavedApplyJobSerializer(all_saved_jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        user_data = request.data
        apply_job = user_data.get('apply_job')
        SavedApplyJob.objects.create(apply_job=apply_job)
        return Response(200)


class showTopJobs(APIView):
    def get(self, request): 
        top_scores = (Jobs.objects
                     .order_by('-id')
                     .values_list('id', flat=True)
                     .distinct())
        job = Jobs.objects.order_by('id').filter(id__in=top_scores[:4])
        #job = Jobs.objects.all()
        serializer = JobSerializer(job, many=True)
        return Response(serializer.data)


class ChangePassword(APIView):
    def get(self, request):
        pass

    def post(self, request):
        user_data = request.data
        user_id = user_data.get('user_id')
        old_password = user_data.get('old_password')
        new_password = user_data.get('new_password')
        re_new_password = user_data.get('re_new_password')
        user_profile = Users.objects.filter(id=user_id, password=old_password)
        if user_profile and new_password == re_new_password:
            Users.objects.filter(id=user_id).update(password=new_password)
            return Response(200)
        elif user_profile and new_password != re_new_password:
            return Response("Password Doesn't Match")
        else:
            return Response("No User Found with this id and password")


class candidate_intro(APIView):
    def get(self, request):
        candidates_intro = CandidateIntro.objects.all()
        serializer = CandidateIntroSerializer(candidates_intro, many=True)
        return Response(serializer.data)

    def post(self, request):
        user_data = request.data
        video_link = user_data.get('video_link')
        question = user_data.get('question')

        user_id = user_data.get('user_id')

        user = Company.objects.get(id=user_id)

        user_profile = Users.objects.create(user=user, video_link=video_link, question=question)

        #serializer = CandidateIntroSerializer(user_profile, many=True)
        
        return Response(200)

class UpdateApplicationStatus(APIView):
    def get(self, request):
        pass

    def post(self, request):

        user_data = request.data
        is_seen = user_data.get('is_seen')
        is_evaluation = user_data.get('is_evaluation')
        is_interview = user_data.get('is_interview')
        is_offer = user_data.get('is_offer')
        apply_job_id = user_data.get('apply_job_id')
        if is_seen:
            ApplyJob.objects.filter(id=apply_job_id).update(is_seen=is_seen)
        if is_evaluation:
            ApplyJob.objects.filter(id=apply_job_id).update(is_evaluation=is_evaluation)
        if is_interview:
            ApplyJob.objects.filter(id=apply_job_id).update(is_interview=is_interview)
        if is_offer:
            ApplyJob.objects.filter(id=apply_job_id).update(is_offer=is_offer)

        return Response(200)


class UserNotifications(APIView):

    def get(self, request):
        user_data = request.query_params
        user_id = user_data.get('user_id')
        user = Users.objects.get(id=user_id)
        notifications = Notifications.objects.filter(user=user, is_read= False)
        serializer = NotificationsSerializer(notifications, many=True)
        response = Response(serializer.data)
        Notifications.objects.filter(user=user, is_read=False).update(is_read=True)
        return response

    def post(self, request):

        user_data = request.data
        user_id = user_data.get('user_id')
        notification = user_data.get('notification')
        user = Users.objects.get(id=user_id)
        Notifications.objects.create(user=user, notification=notification)

        return Response(200)

class UserSettings(APIView):

    def get(self, request):
        user_data = request.query_params
        user_id = user_data.get('user_id')
        user = Users.objects.get(id=user_id)
        settings = Settings.objects.filter(user=user)
        serializer = SettingsSerializer(settings, many=True)
        return Response(serializer.data)

    def post(self, request):

        # pass
        user_data = request.data
        user_id = user_data.get('user_id')
        user = Users.objects.get(id=user_id)
        Settings.objects.create(user=user, user_status='looking_for_a_job')

        return Response(200)

    def put(self, request):

        user_data = request.data
        user_id = user_data.get('user_id')
        vacany_suggestions = user_data.get('vacany_suggestions')
        application_status = user_data.get('application_status')
        newsletter_promotions = user_data.get('newsletter_promotions')
        user_status = user_data.get('user_status')
        user_picture = user_data.get('user_picture')
        user = Users.objects.get(id=user_id)
        Settings.objects.filter(user=user).update(vacany_suggestions=vacany_suggestions, application_status=application_status,
                                newsletter_promotions=newsletter_promotions, user_status=user_status, user_picture=user_picture)

        return Response(200)

class SendEmail(APIView):
    def get(self, request):
        pass

    def post(self, request):
        # pass
        user_data = request.data
        subject = user_data.get('subject')
        email = user_data.get('email')
        message = user_data.get('message')
        general_send_email(email, subject, message)

        return Response(200)