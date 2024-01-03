from django.contrib import admin
from django.urls import path
from . import views
from . import apis

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name='index'),
    path('login', views.Login, name='login'),
    path('about', views.About, name='about'),
]

urlpatterns += [
  path('api/register', apis.Register.as_view()),
]