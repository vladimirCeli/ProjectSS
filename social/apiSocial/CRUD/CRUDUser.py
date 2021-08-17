from rest_framework.views import  APIView
from rest_framework.response import Response
from social.models import User
from social.apiSocial.serializers import UserSerializer


class GETUser(APIView):
    def get(self, request):
        user = User.objects.all()
        profile_serializer = UserSerializer(user, many=True)
        return Response(profile_serializer.data)
