from django.shortcuts import render, redirect,HttpResponse
from django.core.paginator import Paginator
from .models import Book
from datetime import datetime

def home_page(request):
    return redirect('/books/')


def books_view(request):
    books_db = Book.objects.all()
    template = 'books/books_list.html'
    books_list = []
    for book in books_db:
        books_list.append({'name':book.name,'author':book.author,'date':str(book.pub_date)})
    context = {'books':books_list}
    return render(request, template, context)

def book_by_date_view(request,date):
    template = 'books/book_by_date_view.html'
    try:
        date = datetime.strptime(date,'%Y-%m-%d').date()
    except:
        return redirect('/books/')

    books_db = Book.objects.filter(pub_date = date)
    books_list = []
    for book in books_db:
        books_list.append({'name':book.name,'author':book.author,'date':str(book.pub_date)})
    
    page = {}
    page['number'] = str(date)
    try:
        page['next'] = str(Book.objects.filter(pub_date__gt = date)[0].pub_date)
    except:
        pass
    try:
        page['previous'] = str(Book.objects.filter(pub_date__lt = date)[0].pub_date)
    except:
        pass
    context = {'books':books_list,'page':page}

    return render(request, template, context)

