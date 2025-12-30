from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_view, name='books_index'),
    path('<int:book_id>/', views.show_book, name='show_book'),
    path('new/', views.new_view, name='new_book'),
    path('create/', views.create_view, name='create_book'),
    path('edit/<int:book_id>/', views.edit_view, name='edit_book'),
    path('update/<int:book_id>/', views.update_view, name='update_book'),
    path('delete/<int:book_id>/', views.delete_view, name='delete_book'),
]