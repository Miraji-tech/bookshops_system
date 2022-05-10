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
    path('category-list', views.category_view, name='category-list'),
    path('add-category', views.add_category, name='add-category'),
    path('update-category', views.update_category, name='update-category'),
    path('update_category/<category_id>', views.update_category, name='update-category'),
    path('delete-category/<category_id>', views.delete_category, name='delete-category'),
    path('show-category/<category__id>', views.books_in_category, name='show-category'),
]
