from django_ratelimit.decorators import ratelimit
from .common_response import JsonResponseWrapper
from rest_framework import status
from inertia import render
from .utils import JWTGetUserData, JWTGetUserID
from django.db import connection, OperationalError, Error
from .serializers import *
from perpus import settings

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
  
  return render(request, 'about', props={
    'title': 'Tentang Kami'
  })

@ratelimit(key='user_or_ip', rate='30/m')
def Contact(request):
  if request.method != 'GET':
    return JsonResponseWrapper.errormethod()
  
  return render(request, 'contact', props={
    'title': 'Kontak Kami'
  })

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
  
  query = '''SELECT perpus_buku.id AS id, judul, rilis, thumbnail, slug, deskripsi, nama AS penulis
            FROM perpus_buku JOIN perpus_penulis
            WHERE perpus_buku.penulis_id = perpus_penulis.id
            AND slug = %s'''
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
    'book': book
  })
  resp.status_code = 200
  return resp

@ratelimit(key='user_or_ip', rate='30/m')
def Peminjaman(request):
  if request.method != 'GET':
    return JsonResponseWrapper.errormethod()
  
  user_id = JWTGetUserID(request)
  if user_id == '':
    resp = JsonResponseWrapper.error(message="User ID not found, login required !", errors='Unauthorized', status_code=status.HTTP_401_UNAUTHORIZED)
    resp.delete_cookie(settings.JWT['AUTH_COOKIE'])

  peminjaman = []
  query = '''SELECT
              perpus_peminjaman.id AS `id`,
              perpus_buku.judul AS `buku`,
              perpus_peminjaman.tgl_pinjam,
              perpus_peminjaman.tgl_kembali,
              perpus_buku.slug,
              perpus_peminjaman.dikembalikan
            FROM `perpus_peminjaman`
            JOIN perpus_user, perpus_buku
            WHERE perpus_user.id = perpus_peminjaman.user_id
	            AND perpus_buku.id = perpus_peminjaman.buku_id
              AND perpus_user.id = %s
            ORDER BY perpus_peminjaman.tgl_pinjam DESC
          '''
  
  c = connection.cursor()
  isError = False; sqlData = None
  try:
    c.execute(query, (user_id,))
    sqlData = c.fetchall()
    pass
  except OperationalError as e:
    isError = True
  except Error as e:
    isError = True
  except:
    isError = True
  finally:
    c.close()
    
  if isError:
    peminjaman = []

  peminjaman_list = [
    {'id': item[0], 'buku': item[1], 'tgl_pinjam': item[2], 'tgl_kembali': item[3], 'slug': item[4], 'dikembalikan': item[5]} for item in sqlData
  ]
  serial_peminjaman = Serial_Peminjaman(data=peminjaman_list, many=True)
  if serial_peminjaman.is_valid():
    peminjaman = serial_peminjaman.data
  else:
    print(serial_peminjaman.errors)
    peminjaman = []
  
  return render(request, 'peminjaman', props={
    'title': 'Peminjaman',
    'peminjaman': peminjaman
  })

@ratelimit(key='user_or_ip', rate='30/m')
def Notifikasi(request):
  if request.method != 'GET':
    return JsonResponseWrapper.errormethod()
  
  user_id = JWTGetUserID(request)
  query = '''SELECT id, pesan, tanggal, dibaca
          FROM perpus_notifikasi
          WHERE perpus_notifikasi.user_id = %s AND tanggal <= NOW()
          ORDER BY tanggal DESC LIMIT 20'''
  c = connection.cursor()
  isError = False; sqlData = None
  try:
    c.execute(query, (user_id,))
    sqlData = c.fetchall()
    pass
  except OperationalError as e:
    isError = True
  except Error as e:
    isError = True
  except:
    isError = True
  finally:
    c.close()
  
  notifikasi = []
  if sqlData == None or isError == True:
    notifikasi = []
  
  notifikasi_list = [
    {'id': item[0], 'pesan': item[1], 'tanggal': item[2], 'dibaca': item[3]} for item in sqlData
  ]
  serial_notif = Serial_Notifikasi(data=notifikasi_list, many=True)
  if serial_notif.is_valid():
    notifikasi = serial_notif.data
  else:
    notifikasi = []

  return render(request, 'notifikasi', props={
    'title': 'Notifikasi',
    'notifikasi': notifikasi
  })

@ratelimit(key='user_or_ip', rate='30/m')
def Profile(request):
  if request.method != 'GET':
    return JsonResponseWrapper.errormethod()
  
  return render(request, 'profile', props={
    'title': 'Profil',
    'user': JWTGetUserData(request)
  })

@ratelimit(key='user_or_ip', rate='30/m')
def Koleksi(request):
  if request.method != 'GET':
    return JsonResponseWrapper.errormethod()
  
  return render(request, 'koleksi', props={
    'title': 'Koleksi'
  })

@ratelimit(key='user_or_ip', rate='30/m')
def Help(request):
  if request.method != 'GET':
    return JsonResponseWrapper.errormethod()
  
  return render(request, 'help', props={
    'title': 'Pusat Bantuan'
  })

def Search(request):
  if request.method != 'GET':
    return JsonResponseWrapper.errormethod()

  SEARCH = request.GET.get('query', '')
  PAGE = int(request.GET.get('page', 1))
  
  query = '''SELECT B.id, B.judul, B.rilis, B.thumbnail, B.slug, P.nama AS `penulis`
            FROM perpus_buku B
            LEFT JOIN perpus_penulis P ON B.penulis_id = P.id'''
  
  if SEARCH != '':
    query = query + ''' WHERE B.judul LIKE '%''' + SEARCH + '''%'
            LIMIT 20 OFFSET ''' + str((PAGE - 1) * 20)
  else:
    query = query + ''' LIMIT 20 OFFSET ''' + str((PAGE - 1) * 20)
            
  c = connection.cursor()
  isError = False; sqlData = None
  try:
    c.execute(query)
    sqlData = c.fetchall()
    pass
  except Exception as e:
    isError = True
  finally:
    c.close()
  
  booksResult = []
  if not isError:
    row_headers=[x[0] for x in c.description]
    for result in sqlData:
      booksResult.append(dict(zip(row_headers, result)))
  
  resp = render(request, 'search', props={
    'title': 'Cari Buku',
    'books': booksResult
  })
  resp.status_code = status.HTTP_200_OK
  return resp

# ERROR Pages
@ratelimit(key='user_or_ip', rate='30/m')
def Handler404(request, exception):
  if request.method != 'GET':
    return JsonResponseWrapper.errormethod()
  
  resp = render(request, '_404', props={
    'title': '404 Page not found'
  })
  resp.status_code = status.HTTP_404_NOT_FOUND
  return resp