from django_ratelimit.decorators import ratelimit
from .common_response import JsonResponseWrapper
from rest_framework import status
from inertia import render
from .utils import JWTGetUserData
from django.db import connection, OperationalError, Error
from .serializers import *

def ratelimited_error(request, exception):
  return JsonResponseWrapper.error(
    errors='Too many requests !',
    message='Please try again later.',
    status_code=status.HTTP_429_TOO_MANY_REQUESTS
  )

@ratelimit(key='user_or_ip', rate='30/m')
def Index(request):
  if request.method != 'GET':
    return JsonResponseWrapper.errormethod()
  
  return render(request, 'index', props={
    'title': 'Beranda',
    'user': JWTGetUserData(request)
  })

@ratelimit(key='user_or_ip', rate='30/m')
def Login(request):
  if request.method != 'GET':
    return JsonResponseWrapper.errormethod()
  
  return render(request, 'authlogin', props={
    'title': 'Login'
  })

@ratelimit(key='user_or_ip', rate='30/m')
def Register(request):
  if request.method != 'GET':
    return JsonResponseWrapper.errormethod()
  
  return render(request, 'authregister', props={
    'title': 'Register'
  })

@ratelimit(key='user_or_ip', rate='30/m')
def About(request):
  if request.method != 'GET':
    return JsonResponseWrapper.errormethod()
  
  return render(request, 'about')

@ratelimit(key='user_or_ip', rate='30/m')
def Books(request):
  if request.method != 'GET':
    return JsonResponseWrapper.errormethod()
  
  return render(request, 'books', props={
    'title': 'Buku'
  })

@ratelimit(key='user_or_ip', rate='30/m')
def Book(request, id):
  if request.method != 'GET':
    return JsonResponseWrapper.errormethod()
  
  query = '''SELECT judul, rilis, thumbnail, slug, deskripsi, nama AS penulis
            FROM perpus_buku JOIN perpus_penulis
            WHERE perpus_buku.penulis_id = perpus_penulis.id
            AND slug = %s LIMIT 1'''
  c = connection.cursor()
  isError = False; sqlData = None
  try:
    c.execute(query, (id,))
    sqlData = c.fetchone()
    pass
  except OperationalError as e:
    isError = True
  except Error as e:
    isError = True
  except:
    isError = True
  finally:
    c.close()
  
  book = {}
  if sqlData != None:
    row_headers = [x[0] for x in c.description]
    book = dict(zip(row_headers, sqlData))
  
  if isError:
    book = {}
  
  resp = render(request, 'book', props={
    'book': book,
    'title': book['judul']
  })
  resp.status_code = 200
  return resp

@ratelimit(key='user_or_ip', rate='30/m')
def Peminjaman(request):
  if request.method != 'GET':
    return JsonResponseWrapper.errormethod()
  
  return render(request, 'peminjaman', props={
    'title': 'Peminjaman'
  })