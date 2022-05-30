from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name= "library"

urlpatterns = [
    path('all-books/', views.book_info, name='all_books'),
    path('add-book/', views.add_book, name='add_book')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
