from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import categoryForm
from .models import category
from book.models import books


@login_required
def category_view(request):
    cate = category.objects.all()

    context = {
        'category': cate,
    }

    return render(request, 'category/category.html', context)


@login_required
def add_category(request):
    form = categoryForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Congratulation! New category has been created successfully")
        return redirect('add-category')

    context = {
        'form': form,
    }

    return render(request, 'category/add_category.html', context)


@login_required
def update_category(request, category_id):
    category_up = category.objects.get(pk=category_id)
    form = categoryForm(request.POST or None, instance=category_up)
    if form.is_valid():
        form.save()
        return redirect('category-list')

    context = {
        'form': form,
    }

    return render(request, 'category/update_category.html', context)


@login_required
def delete_category(request, category_id):
    category_del = category.objects.get(pk=category_id)
    category_del.delete()
    return redirect('category-list')


@login_required
def books_in_category(request, category__id):
    category_done = category.objects.get(pk=category__id)
    b_in_category = books.objects.filter(book_category_id=category_done)

    context = {
        'category': category_done,
        'books': b_in_category,
    }

    return render(request, 'category/books_in_category.html', context)
