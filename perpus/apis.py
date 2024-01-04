import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .common_response import JsonResponseWrapper
from .models import *
from django.db import connection

class Register(APIView):
  def post(self, request):
    serializer = Serial_Register(data=request.data)
    if serializer.is_valid():
      anggota_id = uuid.uuid4()
      query = ''' INSERT INTO perpus_anggota
        (id, nama, jenis_kelamin, alamat, email, telepon, password)
        VALUES (%s, %s, %s, %s, %s, %s, %s)'''
      try:
        with connection.cursor() as cursor:
          cursor.execute(query, (
            anggota_id,
            serializer.data['nama'],
            serializer.data['jenis_kelamin'],
            serializer.data['alamat'],
            serializer.data['email'],
            serializer.data['telepon'],
            serializer.data['password']
          ))
          return JsonResponseWrapper.created(data=serializer.data, message="Register successful !")
      except Exception as e:
        return JsonResponseWrapper.errorserver(message="Register failed !", errors=str(e))
      
class Login(APIView):
  def post(self, request):
    serializer = Serial_Login(data=request.data)
    if serializer.is_valid():
      return JsonResponseWrapper.created(data=serializer.data, message="Login successful !")
    return JsonResponseWrapper.error(message="Login failed !", errors=serializer.errors)