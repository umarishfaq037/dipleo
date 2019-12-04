from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Users
from .serializers import UserSerializer

class UsersList(APIView):
    def get(self, request):
        users_list = Users.objects.all()
        serializer = UserSerializer(users_list, many=True)
        return Response(serializer.data)

    def post(self):
        pass
