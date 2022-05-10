from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import bookForm
from .models import books
from book_shop.models import book_shop
from django.contrib.auth.models import User


# Create your views here.
@login_required
def add_book(request):
    form = bookForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Congratulation! New book has been added successfully")
        return redirect('add-book')

    context = {
        'form': form,
    }

    return render(request, 'book/add_book.html', context)


@login_required
def books_view(request):
    book_s = books.objects.all()

    context = {
        'books': book_s,
    }

    return render(request, 'book/books.html', context)


@login_required
def update_book(request, book_id):
    book_up = books.objects.get(pk=book_id)
    form = bookForm(request.POST or None, instance=book_up)
    if form.is_valid():
        form.save()
        return redirect('books-list')

    context = {
        'form': form,
    }

    return render(request, 'book/update_book.html', context)


@login_required
def delete_book(request, book_id):
    book_del = books.objects.get(pk=book_id)
    book_del.delete()
    return redirect('book-list')


@login_required
def user_books_view(request):
    book_s = books.objects.filter(id=request.user.id)

    context = {
        'books': book_s,
    }

    return render(request, 'book/books.html', context)