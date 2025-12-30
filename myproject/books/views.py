from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from authors.models import Author
from loans.models import Loan
from categories.models import Category
from .forms import BookForm

# Create your views here.
def books_view(request):
    """_summary_
    Docstring pour hello_books_view

    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        Rendered HTML page with a list of books.
    """
    books = Book.objects.all()
    total_books = books.count()
    available_books = books.filter(copies_available__gt=0).count()
    total_authors = Author.objects.count()
    categories = Category.objects.distinct().all()
    total_categories = categories.count()
    status_loans = Loan.STATUS_CHOICES

    return render(request, 'books/index.html', {
        'books': books, 
        'total_books': total_books, 
        'available_books': available_books, 
        'total_authors': total_authors, 
        'categories': categories,
        'total_categories': total_categories,
        'status_loans': status_loans
        })

def show_book(request, book_id):
    """_summary_
    Docstring pour show_book

    Args:
        request (HttpRequest): The HTTP request object.
        book_id (int): The ID of the book to display.
    
    Returns:
        HttpResponse: The HTTP response with the book details.
    """
    book = Book.objects.get(id=book_id)
    loans = Loan.objects.filter(book=book, return_date__isnull=True)

    return render(request, 'books/show.html', {'book': book, 'loans': loans})

def new_view(request):
    """_summary_
    Docstring pour new_view

    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: The HTTP response for the new book page.
    """
    form = BookForm()

    return render(request, 'books/new.html', {'form': form})

def create_view(request):
    """_summary_
    Docstring pour create_view

    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: The HTTP response after creating a new book.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            new_book = form.save()
            return render(request, 'books/show.html', {'book': new_book})
        else:
            return render(request, 'books/new.html', {'form': form})
    else:
        return HttpResponse('Invalid request method.', status=400)

def edit_view(request, book_id):
    """_summary_
    Docstring pour edit_view

    Args:
        request (HttpRequest): The HTTP request object.
        book_id (int): The ID of the book to edit.
    
    Returns:
        HttpResponse: The HTTP response for the edit book page.
    """
    book = Book.objects.get(id=book_id)
    form = BookForm(instance=book)

    return render(request, 'books/edit.html', {'form': form, 'book': book})

def update_view(request, book_id):
    """_summary_
    Docstring pour update_view

    Args:
        request (HttpRequest): The HTTP request object.
        book_id (int): The ID of the book to update.
    
    Returns:
        HttpResponse: The HTTP response after updating the book.
    """
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            updated_book = form.save()
            return render(request, 'books/show.html', {'book': updated_book})
        else:
            return render(request, 'books/edit.html', {'form': form, 'book': book})
    else:
        return HttpResponse('Invalid request method.', status=400)
    
def delete_view(request, book_id):
    """_summary_
    Docstring pour delete_view

    Args:
        request (HttpRequest): The HTTP request object.
        book_id (int): The ID of the book to delete.
    
    Returns:
        HttpResponse: The HTTP response after deleting the book.
    """
    book = Book.objects.get(id=book_id)
    book.delete()
    
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})
    