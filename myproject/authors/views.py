from django.shortcuts import render
from authors.models import Author

# Create your views here.

def index(request):
    authors = Author.objects.all()

    return render(request, 'authors/index.html', {'authors': authors})

def show_author(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'authors/show.html', {'author': author})

def new_view(request):
    return render(request, 'authors/new.html')

def create_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        birth_date = request.POST.get('birth_date')
        nationality = request.POST.get('nationality')
        author = Author(
            name=name, 
            birth_date=birth_date, 
            nationality=nationality
        )
        author.save()
        return render(request, 'authors/show.html', {'author': author})