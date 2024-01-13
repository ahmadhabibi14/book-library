import bcrypt
import jwt
from perpus import settings
from django.db import connection

def hashPassword(password) -> bytes:
  bytePassword = password.encode('utf-8')
  salt = bcrypt.gensalt()

  hash = bcrypt.hashpw(bytePassword, salt)
  return hash

def verifyPassword(input_password, hashed_password) -> bool:
  # Check if the input password matches the hashed password
  return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password.encode('utf-8'))

def JWTGetUserData(request) -> dict:
  token = request.COOKIES.get('access_token', None)
  decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
  user_id = decoded_token['id']

  userData = {}
  query = 'SELECT nama, email, jenis_kelamin, alamat, telepon, petugas FROM perpus_user WHERE id = %s'
  c = connection.cursor()
  try:
    c.execute(query, (user_id,))
    row_headers=[x[0] for x in c.description]
    res = c.fetchone()
    userData = dict(zip(row_headers, res))
    pass
  except:
    userData = {}
  finally:
    c.close()
  
  return userData