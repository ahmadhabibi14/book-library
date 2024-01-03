from inertia import render
from .models import Anggota

def Index(request):
  anggota = Anggota.objects.all()
  return render(request, 'index', props={
    "anggota": anggota
  })

def Login(request):
  return render(request, 'authlogin')

def About(request):
  return render(request, 'about')