from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AnggotaSerializer
from .common_response import JsonResponseWrapper

class Register(APIView):
  def post(self, request):
    serializer = AnggotaSerializer(data=request.data)
    if serializer.is_valid():
      return JsonResponseWrapper.created(data=serializer.data, message="Register successful !")
    return JsonResponseWrapper.error(message="Register failed !", errors=serializer.errors)