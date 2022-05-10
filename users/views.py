from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import add_userForm
from book_shop.models import book_shop
from book.models import books
from category.models import category


# Create your views here.

@login_required
def index(request):
    shop_count = book_shop.objects.all().count()
    book_count = books.objects.count()
    no_user = User.objects.count()
    category_count = category.objects.count()
    b = books.objects.all()

    context = {
        'shop_count': shop_count,
        'book_count': book_count,
        'no_user': no_user,
        'category_count': category_count,
        'books': b,
    }
    return render(request, 'users/dashboard.html', context)


@login_required
def add_user(request):
    if request.method == "POST":
        form = add_userForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New User has been added successfully")
            return redirect('add-user')
    else:
        form = add_userForm()

    return render(request, 'users/add_user.html', {'form': form})


@login_required
def users(request):

    obj_user = User.objects.all()

    context = {
        'User': obj_user,
    }
    return render(request, 'users/users.html', context)


@login_required
def update_user(request, user_id):
    user_view = User.objects.get(pk=user_id)
    form = add_userForm(request.POST or None, instance=user_view)
    if form.is_valid():
        form.save()
        return redirect('users-list')

    return render(request, 'users/update_user.html', {'form': form})


@login_required
def delete_user(request, user_id):
    user_del = User.objects.get(pk=user_id)
    user_del.delete()
    return redirect('users-list')
