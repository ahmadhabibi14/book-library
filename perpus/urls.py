from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views
from . import apis

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name='index'),
    path('login', views.Login, name='login'),
    path('about', views.About, name='about'),
]

urlpatterns += [
  path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/register', apis.Register.as_view()),
  path('api/login', apis.Login.as_view()),
]