from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, Author, Shelf


def index(request):
    if request.method == "GET":
        return HttpResponse("Hello, world. You're at the todo index.")


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_detail.html', {'book': book})

def author_detail(request, author_id):
    author = Author.objects.get(pk=author_id)
    return render(request, 'author_detail.html', {'author': author})

def author_books(request, author_id):
    author = Author.objects.get(pk=author_id)
    books = Book.objects.filter(author=author)
    return render(request, 'author_books.html', {'author': author, 'books': books})
