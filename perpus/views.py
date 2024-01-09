from django_ratelimit.decorators import ratelimit
from .common_response import JsonResponseWrapper
from rest_framework import status
from inertia import render
from .models import Anggota

def ratelimited_error(request, exception):
  return JsonResponseWrapper.error(
    errors="Too many requests !",
    message="Please try again later.",
    status_code=status.HTTP_429_TOO_MANY_REQUESTS
  )

@ratelimit(key='user_or_ip', rate='30/m')
def Index(request):
  if request.method != 'GET':
    return JsonResponseWrapper.errormethod()
  
  anggota = Anggota.objects.all()
  return render(request, 'index', props={
    "anggota": anggota
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
