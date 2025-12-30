from django.urls import path
from . import views

urlpatterns = [
    path('', views.loans_view, name='loans_index'),
    path('<int:loan_id>/', views.show_loan, name='show_loan'),
    path('new/', views.new_loan, name='new_loan'),
    path('create/', views.create_loan, name='create_loan'),
    path('edit/<int:loan_id>/', views.edit_loan, name='edit_loan'),
    path('update/<int:loan_id>/', views.update_loan, name='update_loan'),
    path('delete/<int:loan_id>/', views.delete_loan, name='delete_loan'),
]