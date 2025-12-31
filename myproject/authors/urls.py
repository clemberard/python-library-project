from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='authors_index'),
    path('<int:author_id>/', views.show_author, name='show_author'),
    path('new/', views.new_view, name='new_author'),
    path('create/', views.create_view, name='create_author'),
    path('edit/<int:author_id>/', views.edit_view, name='edit_author'),
    path('update/<int:author_id>/', views.update_view, name='update_author')
]