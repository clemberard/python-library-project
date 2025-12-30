from django.shortcuts import render
from authors.models import Author
from .forms import AuthorForm

# Create your views here.

def index(request):
    authors = Author.objects.all()

    return render(request, 'authors/index.html', {'authors': authors})

def show_author(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'authors/show.html', {'author': author})

def new_view(request):
    form = AuthorForm()
    return render(request, 'authors/new.html', {'form': form})

def create_view(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            author = Author(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                birth_date=form.cleaned_data['birth_date'],
                nationality=form.cleaned_data['nationality'],
                biography=form.cleaned_data['biography'],
                death_date=form.cleaned_data['death_date'],
                website=form.cleaned_data['website'],
                photo=form.cleaned_data['photo'].read() if form.cleaned_data['photo'] else None
            )
            author.save()
            return render(request, 'authors/show.html', {'author': author})
    else:
        form = AuthorForm()