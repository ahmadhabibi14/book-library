from django.contrib import admin
from django.urls import path
from . import views
from . import apis
from perpus import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name='index'),
    path('login', views.Login, name='login'),
    path('register', views.Register, name='register'),
    path('about', views.About, name='about'),
    path('contact', views.Contact, name='contact'),
    path('books', views.Books, name='books'),
    path('books/<str:id>/', views.Book, name='book'),
    path('peminjaman', views.Peminjaman, name='peminjaman'),
    path('notifikasi', views.Notifikasi, name='notifikasi'),
    path('profile', views.Profile, name='profile'),
    path('koleksi', views.Koleksi, name='koleksi'),
    path('help', views.Help, name='help'),
    path('search', views.Search, name='search'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
  path('api/register', apis.Register.as_view()),
  path('api/login', apis.Login.as_view()),
  path('api/books', apis.Books.as_view()),
  path('api/pinjam-buku', apis.PinjamBuku.as_view()),
  path('api/kembalikan-buku', apis.KembalikanBuku.as_view()),
  path('api/total-notifikasi', apis.TotalNotifikasi.as_view()),
  path('api/hapus-notifikasi', apis.HapusNotifikasi.as_view()),
  path('api/edit-profile', apis.EditProfile.as_view()),
  path('api/debug', apis.Debug.as_view()),
  path('api/debug-sse', apis.DebugSSE),
]

handler404 = views.Handler404