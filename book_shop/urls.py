"""online_bookshops_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('add-bookshop', views.add_book_shop, name='add-bookshop'),
    path('book_shops', views.display_book_shops, name='book-shops'),
    path('update-bookshop/<book_shop_id>', views.update_book_shop, name='update-bookshop'),
    path('delete-bookshop/<book_shop_id>', views.delete_book_shop, name='delete-bookshop'),
    path('show-bookshop/<book_shop_id>', views.show_book_shops, name='show-bookshop'),
    path('books_in_user_bookshop/<book_shop_id>', views.show_books_in_user_bookshop, name="user-books-in-bookshops"),
]
