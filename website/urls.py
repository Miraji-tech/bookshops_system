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
    path('', views.homepage, name='home'),
    path('books', views.books_available, name='books'),
    path('search', views.search_book, name='search_books'),
    path('Display_category/<category__id>', views.books_by_category, name='Display_category'),
    path('View_bookshop/<book_shop_id>', views.render_bookshops, name='View_bookshop'),
]
