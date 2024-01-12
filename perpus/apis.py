import datetime
import uuid
import json
import jwt
from rest_framework.views import APIView
from rest_framework.throttling import AnonRateThrottle
from .models import *

from perpus import settings
from .serializers import *
from .common_response import JsonResponseWrapper
from .utils import hashPassword, verifyPassword
from .models import *
from django.db import connection, OperationalError, Error

class Register(APIView):
  throttle_classes = [AnonRateThrottle]
  def post(self, request):
    serializer = Serial_Register(data=request.data)
    if serializer.is_valid():
      user_id = str(uuid.uuid4())
      user_password = hashPassword(serializer.data['password'])
      query = ''' INSERT INTO perpus_user
        (id, nama, jenis_kelamin, alamat, email, telepon, password)
        VALUES (%s, %s, %s, %s, %s, %s, %s)'''
      c = connection.cursor()
      isError = False; errorState = ''
      try:
        c.execute(query, (
          str(user_id),
          serializer.data['nama'],
          serializer.data['jenis_kelamin'],
          serializer.data['alamat'],
          serializer.data['email'],
          serializer.data['telepon'],
          user_password
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
      
      token = jwt.encode({
        'id': user_id,
        'iat': datetime.datetime.utcnow(),
        'nbf': datetime.datetime.utcnow() + datetime.timedelta(minutes=-5),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(weeks=16)
      }, settings.SECRET_KEY)

      resp = JsonResponseWrapper.created(
        data={
          'token': token,
          'user': serializer.data
        },
        message="Register successful !"
      )
      resp.set_cookie(
        key=settings.JWT['AUTH_COOKIE'],
        value=token,
        expires=settings.JWT['ACCESS_TOKEN_LIFETIME'],
        secure=settings.JWT['AUTH_COOKIE_SECURE'],
        httponly=settings.JWT['AUTH_COOKIE_HTTP_ONLY'],
        samesite=settings.JWT['AUTH_COOKIE_SAMESITE']
      )
      return resp
    else:
      return JsonResponseWrapper.error(message="Register failed !", errors=serializer.errors)
      
class Login(APIView):
  throttle_classes = [AnonRateThrottle]
  def post(self, request):
    body = json.loads(request.body.decode("utf-8"))
    email = body['email']
    password = body['password']
    if email is None or password is None:
      return JsonResponseWrapper.error(message="Email and password are required !")

    query = 'SELECT email, password, id FROM perpus_user WHERE email = %s'
    c = connection.cursor()
    isError = False; errorState = ''; sqlData = None
    try:
      c.execute(query, (email,))
      sqlData = c.fetchone()
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

    if sqlData is None:
      return JsonResponseWrapper.error(message="Email not found !")

    if not verifyPassword(password, sqlData[1]):
      return JsonResponseWrapper.error(message="Wrong password !")

    token = jwt.encode({
      'id': sqlData[2],
      'iat': datetime.datetime.utcnow(),
      'nbf': datetime.datetime.utcnow() + datetime.timedelta(minutes=-5),
      'exp': datetime.datetime.utcnow() + datetime.timedelta(weeks=16)
    }, settings.SECRET_KEY)

    resp = JsonResponseWrapper.success(
      message="Login successful !",
      data={
        'token': token
      }
    )
    resp.set_cookie(
      key=settings.JWT['AUTH_COOKIE'],
      value=token,
      expires=settings.JWT['ACCESS_TOKEN_LIFETIME'],
      secure=settings.JWT['AUTH_COOKIE_SECURE'],
      httponly=settings.JWT['AUTH_COOKIE_HTTP_ONLY'],
      samesite=settings.JWT['AUTH_COOKIE_SAMESITE']
    )
    
    return resp

class Books(APIView):
  throttle_classes = [AnonRateThrottle]
  def post(self, request):
    OFFSET = request.GET.get('offset', 0)
    LIMIT = request.GET.get('limit', 10)

    query = ''' SELECT judul, rilis, thumbnail, nama AS penulis
            FROM perpus_buku JOIN perpus_penulis
            WHERE perpus_buku.penulis_id = perpus_penulis.id
            LIMIT ''' + str(LIMIT) + ''' OFFSET ''' + str(OFFSET)
    c = connection.cursor()
    isError = False; errorState = ''; sqlData = None
    try:
      c.execute(query)
      sqlData = c.fetchall()
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
      return JsonResponseWrapper.errorserver(message="Cannot get books !", errors=errorState)

    books_list = [
      {'judul': item[0], 'rilis': item[1], 'thumbnail': item[2], 'penulis': item[3]} for item in sqlData
    ]
    books = Serial_Books(data=books_list, many=True)
    if books.is_valid():
      return JsonResponseWrapper.success(data=books.data, message="Success !")
    
    return JsonResponseWrapper.error(message="Cannot get books !", errors=books.errors)

class DebugProtect(APIView):
  throttle_classes = [AnonRateThrottle]
  def post(self, request):
    return JsonResponseWrapper.created(message="successful !")