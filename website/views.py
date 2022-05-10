from django.shortcuts import render
from book.models import books
from category.models import category

# Create your views here.
from book_shop.models import book_shop


def homepage(request):
    return render(request, 'website/index.html')


def search_book(request):
    if 'q' in request.GET:
        q = request.GET['q']
        book_title = books.objects.filter(book_name__icontains=q)

    else:
        book_title = books.objects.all()

    context = {
        'books': book_title,
    }
    return render(request, 'website/searched_books.html', context)


def books_available(request):
    book__s = books.objects.all()
    book_cate = category.objects.all()
    all_bookshops = book_shop.objects.all()

    context = {
        'books': book__s,
        'category': book_cate,
        'book_shop': all_bookshops,
    }

    return render(request, 'website/books.html', context)


def books_by_category(request, category__id):
    get_category = category.objects.get(pk=category__id)
    b_by_category = books.objects.filter(book_category_id=get_category)

    context = {
        'category': get_category,
        'books': b_by_category,
    }

    return render(request, 'website/book_by_category.html', context)


def books_by_bookshop(request, category__id):
    get_category = category.objects.get(pk=category__id)
    b_by_category = books.objects.filter(book_category_id=get_category)

    context = {
        'category': get_category,
        'books': b_by_category,
    }

    return render(request, 'website/book_by_category.html', context)


def render_bookshops(request, book_shop_id):
    display_bookshops = book_shop.objects.get(id=book_shop_id)
    view_books = books.objects.filter(bookshop_id=display_bookshops)

    context = {
        'book_shop': display_bookshops,
        'books': view_books,
    }

    return render(request, 'website/book_by_bookshop.html', context)
