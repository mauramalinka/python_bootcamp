from django.shortcuts import render
from books.models import Book

def books_list(request):
    books = Book.objects.all()
    return render(
        template_name="books/books_list.html",
        contex = {"books": books}
    )
# Create your views here.
