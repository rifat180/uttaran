from django.contrib import admin
from .models import (
    LibraryName,
    Mission,
    Vision,
    Goal,
    Testimonial,
    EventPicture,
    Book,
    Member,
    About
)

class TestimonialAdmin(admin.ModelAdmin):
  list_display = ('writer', 'testimonial')

class BookAdmin(admin.ModelAdmin):
  list_display = ('name', 'authorName')

class MemberAdmin(admin.ModelAdmin):
  list_display = ('name', 'designation')

# Register your models here.
admin.site.register(LibraryName)
admin.site.register(Mission)
admin.site.register(Vision)
admin.site.register(Goal)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(EventPicture)
admin.site.register(Book, BookAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(About)

