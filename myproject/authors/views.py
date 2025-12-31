from django.shortcuts import render
from authors.models import Author
from books.models import Book
from .forms import AuthorForm
import datetime

# Create your views here.

def index(request):
    """
    Affiche la liste de tous les auteurs.
    """
    authors = Author.objects.all()
    total_authors = authors.count()
    living_authors = authors.filter(death_date__isnull=True).count()
    nationalities_count = authors.values('nationality').distinct().count()
    total_books = Book.objects.count()

    return render(request, 'authors/index.html', {
        'authors': authors,
        'total_authors': total_authors,
        'living_authors': living_authors,
        'nationalities_count': nationalities_count,
        'total_books': total_books
    })

def show_author(request, author_id):
    """
    Affiche les détails d'un auteur spécifique.
    """
    author = Author.objects.get(id=author_id)
    books = Book.objects.filter(author=author)
    total_pages = sum(book.number_pages for book in books)
    available_books = books.filter(copies_available__gt=0).count()
    if author.death_date:
        author_age = author.death_date.year - author.birth_date.year
    else:
        author_age = current_year - author.birth_date.year

    return render(request, 'authors/show.html', {'author': author, 'books': books, 'total_pages': total_pages, 'available_books': available_books, 'author_age': author_age})

def new_view(request):
    """
    Affiche le formulaire pour créer un nouvel auteur.
    """
    form = AuthorForm()
    return render(request, 'authors/new.html', {'form': form})

def create_view(request):
    """
    Traite le formulaire de création d'un nouvel auteur.
    """
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            author = form.save()
            return render(request, 'authors/show.html', {'author': author})
        else:
            return render(request, 'authors/new.html', {'form': form})
    else:
        form = AuthorForm()
        
def edit_view(request, author_id):
    """
    Affiche le formulaire pour éditer un auteur existant.
    """
    author = Author.objects.get(id=author_id)
    form = AuthorForm(instance=author)
    return render(request, 'authors/edit.html', {'form': form, 'author': author})

def update_view(request, author_id):
    """
    Traite le formulaire de mise à jour d'un auteur existant.
    """
    author = Author.objects.get(id=author_id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            author = form.save()
            return render(request, 'authors/show.html', {'author': author})
        else:
            return render(request, 'authors/edit.html', {'form': form, 'author': author})
    else:
        form = AuthorForm(instance=author)
        return render(request, 'authors/edit.html', {'form': form, 'author': author})
