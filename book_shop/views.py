from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import book_shopsForm
from .models import book_shop
from book.models import books


# create your views here
@login_required
def add_book_shop(request):
    form = book_shopsForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Congratulation! New Bookshop has been added successfully")
        return redirect('add-bookshop')
    context = {

        'form': form,
    }

    return render(request, 'book_shop/add_book_shop.html', context)


@login_required
def display_book_shops(request):

    shops = book_shop.objects.all()

    context = {
        'book_shop': shops,
    }

    return render(request, 'book_shop/book_shops.html', context)


@login_required
def show_book_shops(request, book_shop_id):
    show_shops = book_shop.objects.get(id=book_shop_id)
    show_books = books.objects.filter(bookshop_id=show_shops)

    context = {
        'book_shop': show_shops,
        'books': show_books,
    }

    return render(request, 'book_shop/book_in_bookshop.html', context)


@login_required
def update_book_shop(request, book_shop_id):
    book_shop_up = book_shop.objects.get(pk=book_shop_id)
    form = book_shopsForm(request.POST or None, instance=book_shop_up)
    if form.is_valid():
        form.save()
        return redirect('book-shops')

    context = {
        'form': form,
    }

    return render(request, 'book_shop/update_book_shop.html', context)


@login_required
def delete_book_shop(request, book_shop_id):
    book_shop_del = book_shop.objects.get(pk=book_shop_id)
    book_shop_del.delete()
    return redirect('book-shops')


@login_required
def show_books_in_user_bookshop(request, book_shop_id):
    show_bookshops = book_shop.objects.get(id = book_shop_id, instance=request.user.id)
    show_books = books.objects.filter(book_shop_id=show_bookshops)

    context = {
        'book_hops': show_bookshops,
        'books': show_books,
    }

    return render(request, 'book_shop/book_in_bookshop.html', context)