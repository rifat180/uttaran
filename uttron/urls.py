from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from root.views import (
    home,
    books,
    book_details,
    members,
    member_details,
    about,
    contacts
)

urlpatterns = [
    path('', home, name='home'),
    path('books/', books, name='books'),
    path('books/<int:id>/details', book_details, name='book details'),
    path('members/', members, name='members'),
    path('members/<int:id>/details', member_details, name='members details'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)