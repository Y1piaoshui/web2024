from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/add/', views.book_add, name='book_add'),
    path('authors/', views.author_list, name='author_list'),
    path('borrowers/', views.borrower_list, name='borrower_list'),
    path('borrow/', views.borrow_record_list, name='borrow_record_list'),
    path('borrow/add/', views.borrow_record_add,
         name='borrow_record_add'),  # 新增借阅记录页面
]
