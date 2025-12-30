from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from authors.models import Author
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
    
    return render(request, 'books/index.html', {'books': books})

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
    return render(request, 'books/show.html', {'book': book})

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
        isbn = request.POST.get('isbn')
        title = request.POST.get('title')
        price = request.POST.get('price')
        published_date = request.POST.get('published_date')
        author_id = request.POST.get('author')
        
        author = Author.objects.get(id=author_id)
        
        new_book = Book(
            isbn=isbn,
            title=title,
            price=price,
            published_date=published_date,
            author=author
        )
        new_book.save()
        
        return render(request, 'books/show.html', {'book': new_book})
    else:
        return HttpResponse('Invalid request method.', status=400)