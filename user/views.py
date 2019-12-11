from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Users
from .serializers import UserSerializer
from rest_framework.parsers import JSONParser


class UsersList(APIView):
    def get(self, request):
        users_list = Users.objects.all()
        serializer = UserSerializer(users_list, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class Profile(APIView):
    def post(self, request):
        profile_data = request.data
        print(profile_data)
        print(profile_data.get('name'))
        return Response(200)