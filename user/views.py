from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import UserSerializer
from rest_framework.parsers import JSONParser

class UsersList(APIView):
    def get(self, request):
        users_list = Users.objects.all()
        serializer = UserSerializer(users_list, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class UserProfile(APIView):
    def post(self, request):
        profile_data = request.data
        print(profile_data)
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
        print(user)
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
        return Response(200)