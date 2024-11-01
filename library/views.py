from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author, Borrower, BorrowRecord


def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'library/book_detail.html', {'book': book})


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'library/author_list.html', {'authors': authors})


def borrower_list(request):
    borrowers = Borrower.objects.all()
    return render(request, 'library/borrower_list.html', {'borrowers': borrowers})


def borrow_record_list(request):
    borrow_records = BorrowRecord.objects.all()
    return render(request, 'library/borrow_record_list.html', {'borrow_records': borrow_records})


def book_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_name = request.POST.get('author')  # 获取用户输入的作者名称
        category = request.POST.get('category')
        isbn = request.POST.get('isbn')
        published_date = request.POST.get('published_date')

        # 查找或创建作者对象
        author, created = Author.objects.get_or_create(name=author_name)

        # 创建新的书籍对象
        Book.objects.create(
            title=title,
            author=author,
            category=category,
            isbn=isbn,
            published_date=published_date,
        )

        # 重定向到书籍列表页面
        return redirect('book_list')

    return render(request, 'library/book_add.html')


def borrow_record_list(request):
    borrow_records = BorrowRecord.objects.all()
    return render(request, 'library/borrow_record_list.html', {'borrow_records': borrow_records})


def borrow_record_add(request):
    if request.method == 'POST':
        book_id = request.POST.get('book')
        borrower_name = request.POST.get('borrower')  # 获取输入的借阅者姓名
        due_date = request.POST.get('due_date')

        # 获取书籍对象
        book = Book.objects.get(id=book_id)

        # 查找或创建借阅者
        borrower, created = Borrower.objects.get_or_create(name=borrower_name)

        # 创建借阅记录
        BorrowRecord.objects.create(
            book=book,
            borrower=borrower,
            borrow_date=timezone.now(),
            due_date=due_date
        )

        return redirect('borrow_record_list')

    # 获取所有书籍用于表单选择
    books = Book.objects.all()
    return render(request, 'library/borrow_record_add.html', {'books': books})
