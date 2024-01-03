from inertia import render

def Index(request):
  return render(request, 'index')

def Login(request):
  return render(request, 'authlogin')

def About(request):
  return render(request, 'about')