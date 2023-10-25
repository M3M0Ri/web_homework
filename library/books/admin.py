from django.contrib import admin
from .models import Shelf, Author, Book


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Shelf)
