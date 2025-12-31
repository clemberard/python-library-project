from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from authors.models import Author
from loans.models import Loan
from categories.models import Category
from .forms import BookForm

# Create your views here.
def books_view(request):
    """
    Affiche la liste de tous les livres avec des statistiques supplémentaires.
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
    """
    Affiche les détails d'un livre spécifique, y compris les prêts en cours.
    """
    book = Book.objects.get(id=book_id)
    loans = Loan.objects.filter(book=book, return_date__isnull=True)

    return render(request, 'books/show.html', {'book': book, 'loans': loans})

def new_view(request):
    """
    Affiche le formulaire pour créer un nouveau livre.
    """
    if request.GET.get('author'):
        form = BookForm(initial={'author': request.GET.get('author')})
    else:
        form = BookForm()

    return render(request, 'books/new.html', {'form': form})

def create_view(request):
    """
    Traite le formulaire de création d'un nouveau livre.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            new_book = form.save()
            return render(request, 'books/show.html', {'book': new_book})
        else:
            breakpoint()
            return render(request, 'books/new.html', {'form': form})
    else:
        return HttpResponse('Invalid request method.', status=400)

def edit_view(request, book_id):
    """
    Affiche le formulaire pour éditer un livre existant.
    """
    book = Book.objects.get(id=book_id)
    form = BookForm(instance=book)

    return render(request, 'books/edit.html', {'form': form, 'book': book})

def update_view(request, book_id):
    """
    Traite le formulaire de mise à jour d'un livre existant.
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
    """
    Supprime un livre spécifique.
    """
    book = Book.objects.get(id=book_id)
    book.delete()
    
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})
    