import jwt
from perpus import settings
from .common_response import JsonResponseWrapper
from rest_framework import status
from inertia import render

def JSONWebTokenAuthentication(get_response):
  def middleware(request):
    def renderView():
      return render(request, 'error', props={
        'code': status.HTTP_401_UNAUTHORIZED,
        'status': 'Unauthorized',
        'message': 'Please login first !',
      })
    
    isView = False; isAPI = False; isProtect = False
    if request.path == '/login' or request.path == '/register' or request.path.startswith('/static') or request.path.startswith('/media') or request.path == '/assets':
      return get_response(request)
    
    if request.path.startswith('/'):
      isView = True
      isProtect = True

    if request.path.startswith('/api'):
      return get_response(request)
    
    if request.path == '/api/p/debug-protect':
      print('request.path.startswith(/api/p/)')
      isAPI = True
      isProtect = True
    
    token = request.COOKIES.get('access_token', None)
    if not token:
      token = request.headers.get('Authorization', None)
      if not token:
        if isView and isProtect:
          if request.method != 'GET':
            return JsonResponseWrapper.errormethod()

          return renderView()

        if isAPI and isProtect:
          return JsonResponseWrapper.error(message="Cannot access this endpoint", errors="UNAUTHORIZED", status_code=status.HTTP_401_UNAUTHORIZED) 
        return JsonResponseWrapper.error(message="Cannot access this endpoint", errors="UNAUTHORIZED", status_code=status.HTTP_401_UNAUTHORIZED)
      
      if isAPI and isProtect:
        return JsonResponseWrapper.error(message="Cannot access this endpoint", errors="UNAUTHORIZED", status_code=status.HTTP_401_UNAUTHORIZED) 
    
    try:
      decoded_payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
      request.jwt_payload = decoded_payload
    except jwt.ExpiredSignatureError:
      if isView and isProtect:
        if request.method != 'GET':
          return JsonResponseWrapper.errormethod()

        return renderView()
      
      if isAPI and isProtect:
        return JsonResponseWrapper.error(message="Token has expired", errors="UNAUTHORIZED", status_code=status.HTTP_401_UNAUTHORIZED)
      return JsonResponseWrapper.error(message="Token has expired", errors="UNAUTHORIZED", status_code=status.HTTP_401_UNAUTHORIZED)
    except jwt.InvalidTokenError:
      if isView and isProtect:
        if request.method != 'GET':
          return JsonResponseWrapper.errormethod()

        return renderView()
      
      if isAPI and isProtect:
        return JsonResponseWrapper.error(message="Invalid token", errors="UNAUTHORIZED", status_code=status.HTTP_401_UNAUTHORIZED)
      return JsonResponseWrapper.error(message="Invalid token", errors="UNAUTHORIZED", status_code=status.HTTP_401_UNAUTHORIZED)

    return get_response(request)
  
  return middleware