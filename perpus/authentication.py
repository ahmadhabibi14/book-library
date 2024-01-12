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
    
    isView = False
    if request.path == '/login' or request.path == '/register':
      return get_response(request)
    
    if request.path.startswith('/') and request.method == 'GET':
      isView = True

    if request.path.startswith('/api'):
      return get_response(request)
    
    token = request.COOKIES.get('access_token', None)
    if not token:
      token = request.headers.get('Authorization', None)
      if not token:
        if isView:
          return renderView()
    
    try:
      decoded_payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
      request.jwt_payload = decoded_payload
    except jwt.ExpiredSignatureError:
      if isView:
        return renderView()
      
      return JsonResponseWrapper.error(message="Token has expired", errors="UNAUTHORIZED", status_code=status.HTTP_401_UNAUTHORIZED)
    except jwt.InvalidTokenError:
      if isView:
        return renderView()
      
      return JsonResponseWrapper.error(message="Invalid token", errors="UNAUTHORIZED", status_code=status.HTTP_401_UNAUTHORIZED)

    return get_response(request)
  
  return middleware