from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories_view, name='categories_index'),
    path('new/', views.new_category, name='new_category'),
    path('create/', views.create_category, name='create_category'),
    path('<int:category_id>/', views.show_category, name='show_category'),
]