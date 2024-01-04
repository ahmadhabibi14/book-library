import uuid
from django_ratelimit.decorators import ratelimit
from rest_framework.views import APIView
from .serializers import *
from .common_response import JsonResponseWrapper
from .models import *
from django.db import connection, OperationalError, Error

class Register(APIView):
  @ratelimit(key='user_or_ip', rate='30/m')
  def post(self, request):
    serializer = Serial_Register(data=request.data)
    if serializer.is_valid():
      anggota_id = uuid.uuid4()
      query = ''' INSERT INTO perpus_anggota
        (id, nama, jenis_kelamin, alamat, email, telepon, password)
        VALUES (%s, %s, %s, %s, %s, %s, %s)'''
      c = connection.cursor()
      isError = False; errorState = ''
      try:
        c.execute(query, (
          anggota_id,
          serializer.data['nama'],
          serializer.data['jenis_kelamin'],
          serializer.data['alamat'],
          serializer.data['email'],
          serializer.data['telepon'],
          serializer.data['password']
        ))
        pass
      except OperationalError as e:
        isError = True
        errorState = str(e)
      except Error as e:
        isError = True
        errorState = str(e)
      except:
        isError = True
        errorState = 'Unknown error'
      finally:
        c.close()
      
      if isError:
        return JsonResponseWrapper.errorserver(message="Register failed !", errors=errorState)
      
      return JsonResponseWrapper.created(data=serializer.data, message="Register successful !")
    else:
      return JsonResponseWrapper.error(message="Register failed !", errors=serializer.errors)
      
class Login(APIView):
  def post(self, request):
    serializer = Serial_Login(data=request.data)
    if serializer.is_valid():
      return JsonResponseWrapper.created(data=serializer.data, message="Login successful !")
    return JsonResponseWrapper.error(message="Login failed !", errors=serializer.errors)