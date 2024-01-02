from inertia import render

def index(request):
  return render(request, 'app.html')