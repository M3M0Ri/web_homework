from django.urls import path
from . import views

urlpatterns = [
    path('book/list/', views.book_list, name='book_list'),
    path("", views.index, name="index"),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('author/<int:author_id>/books/', views.author_books, name='author_books'),
]
