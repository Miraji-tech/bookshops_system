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
    path('add-book', views.add_book, name='add-book'),
    path('books-list', views.books_view, name='books-list'),
    path('user-books-list', views.user_books_view, name='user-books-list'),
    path('update-book/<book_id>', views.update_book, name='update-book'),
    path('delete-book/<book_id>', views.delete_book, name='delete-book'),
]
