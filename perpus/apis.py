from datetime import timedelta, datetime
import uuid
import json
import time
import jwt
import asyncio
import random
from rest_framework.views import APIView
from rest_framework.throttling import AnonRateThrottle
from .models import *
from rest_framework import status
from perpus import settings
from .serializers import *
from .common_response import JsonResponseWrapper
from .utils import hashPassword, verifyPassword, JWTGetUserID
from .models import *
from django.db import connection, OperationalError, Error
from django.http import StreamingHttpResponse

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
        'iat': datetime.utcnow(),
        'nbf': datetime.utcnow() + timedelta(minutes=-5),
        'exp': datetime.utcnow() + timedelta(weeks=16)
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
      'iat': datetime.utcnow(),
      'nbf': datetime.utcnow() + timedelta(minutes=-5),
      'exp': datetime.utcnow() + timedelta(weeks=16)
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

    query = ''' SELECT judul, rilis, thumbnail, slug, nama AS penulis
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
      {'judul': item[0], 'rilis': item[1], 'thumbnail': item[2], 'slug': item[3], 'penulis': item[4]} for item in sqlData
    ]
    books = Serial_Books(data=books_list, many=True)
    if books.is_valid():
      return JsonResponseWrapper.success(data=books.data, message="Success !")
    
    return JsonResponseWrapper.error(message="Cannot get books !", errors=books.errors)

class PinjamBuku(APIView):
  throttle_classes = [AnonRateThrottle]
  def post(self, request):
    user_id = JWTGetUserID(request)
    if user_id == '':
      resp = JsonResponseWrapper.error(message="User ID not found, login required !", errors='Unauthorized', status_code=status.HTTP_401_UNAUTHORIZED)
      resp.delete_cookie(settings.JWT['AUTH_COOKIE'])
    
    c = connection.cursor()

    body = json.loads(request.body.decode("utf-8"))
    buku_id = body['buku_id']
    if buku_id == None or '':
      return JsonResponseWrapper.error(message="Buku id tidak ditemukan !", errors='Invalid payload', status_code=status.HTTP_400_BAD_REQUEST)
     
    isError = False
    try:
      c.execute('SELECT user_id, buku_id FROM perpus_peminjaman WHERE user_id = %s AND buku_id = %s', (user_id, buku_id,))
      sqlData = c.fetchone()
      if sqlData != None:
        c.close()
        return JsonResponseWrapper.error(message="Buku sudah dipinjam !", errors='Conflict', status_code=status.HTTP_409_CONFLICT)
      pass
    except Exception as e:
      isError = False
    
    peminjaman_id = str(uuid.uuid4()); notifikasi_id = str(uuid.uuid4())
    tgl_kembali = datetime.utcfromtimestamp(time.time() + 90 * 24 * 60 * 60) # 3 bulan
    query = '''INSERT INTO perpus_peminjaman (id, tgl_pinjam, tgl_kembali, user_id, buku_id, dikembalikan)
            VALUES (%s, CURRENT_TIMESTAMP, %s, %s, %s, FALSE)'''
    query2 = '''INSERT INTO perpus_notifikasi (id, pesan, tanggal, dibaca, user_id)
            VALUES (%s, %s, %s, FALSE, %s)'''
    
    try:
      c.execute(query, ( peminjaman_id, tgl_kembali, user_id, buku_id))
      c.execute(query2, ( notifikasi_id, 'Buku yang anda pinjam melewati batas waktu !!', tgl_kembali, user_id,))
      pass
    except OperationalError as e:
      print(e)
      isError = True
    except Error as e:
      print(e)
      isError = True
    except Exception as e:
      print(e)
      isError = True
    finally:
      c.close()
      
    if isError:
      return JsonResponseWrapper.errorserver(message='Tidak bisa meminjam buku !', errors='Unknown error')
      
    return JsonResponseWrapper.success(message='Berhasil meminjam buku !')

class KembalikanBuku(APIView):
  throttle_classes = [AnonRateThrottle]
  def post(self, request):
    user_id = JWTGetUserID(request)
    if user_id == '':
      resp = JsonResponseWrapper.error(message="User ID not found, login required !", errors='Unauthorized', status_code=status.HTTP_401_UNAUTHORIZED)
      resp.delete_cookie(settings.JWT['AUTH_COOKIE'])
    
    c = connection.cursor()
    body = json.loads(request.body.decode("utf-8"))
    peminjaman_id = body['peminjaman_id']
    if peminjaman_id == None or '':
      return JsonResponseWrapper.error(message="Peminjaman id tidak ditemukan !", errors='Invalid payload', status_code=status.HTTP_400_BAD_REQUEST)

    isError = False
    try:
      c.execute('SELECT id FROM perpus_peminjaman WHERE id = %s', (peminjaman_id,))
      sqlData = c.fetchone()
      if sqlData == None:
        c.close()
        return JsonResponseWrapper.error(message=f"Tidak ada peminjaman dengan ID: {peminjaman_id} !", errors='Invalid payload', status_code=status.HTTP_409_CONFLICT)
      pass
    except Exception as e:
      isError = False
    
    query = '''UPDATE perpus_peminjaman SET dikembalikan = TRUE WHERE id = %s'''
    try:
      c.execute(query, ( peminjaman_id,))
      pass
    except Exception as e:
      isError = True
    finally:
      c.close()
      
    if isError:
      return JsonResponseWrapper.errorserver(message='Tidak bisa mengembalikan buku !', errors='Unknown error')
    
    return JsonResponseWrapper.success(message='Berhasil mengembalikan buku !', data=peminjaman_id)

class TotalNotifikasi(APIView):
  def post(self, request):
    user_id = JWTGetUserID(request)
    if user_id == '':
      resp = JsonResponseWrapper.error(message="User ID not found, login required !", errors='Unauthorized', status_code=status.HTTP_401_UNAUTHORIZED)
      resp.delete_cookie(settings.JWT['AUTH_COOKIE'])
   
    c = connection.cursor()
    query = '''SELECT COUNT(CASE WHEN perpus_notifikasi.dibaca = FALSE
            AND perpus_notifikasi.tanggal <= NOW()
              THEN perpus_notifikasi.id END)
            AS `total_notifikasi` 
            FROM perpus_user LEFT JOIN perpus_notifikasi
            ON perpus_user.id = perpus_notifikasi.user_id
            WHERE perpus_user.id = %s'''
      
    isError = False; errorState = ''; notification = {}
    try:
      c.execute(query, (user_id,))
      row_headers=[x[0] for x in c.description]
      res = c.fetchone()
      notification = dict(zip(row_headers, res))
      pass
    except Exception as e:
      isError = True; errorState = e
    
    if isError:
      return JsonResponseWrapper.errorserver(message="Cannot get notifivation !", errors=errorState)
    
    return JsonResponseWrapper.success(data=notification, message="Success !")

class Debug(APIView):
  throttle_classes = [AnonRateThrottle]
  def post(self, request):
    return JsonResponseWrapper.created(message='successful !')

async def DebugSSE(request):
  async def event_stream():
    emojis = ["🚀", "🐎", "🌅", "🦾", "🍇"]
    i = 0
    while True:
      yield f'data: {random.choice(emojis)} {i}\n\n'
      i += 1
      await asyncio.sleep(5)

  return StreamingHttpResponse(event_stream(), content_type='text/event-stream')