from django.shortcuts import render
from .models import Category
from .forms import CategoryForm

# Create your views here.

def categories_view(request):
    categories = Category.objects.all()
    
    return render(request, 'categories/index.html', {'categories': categories})

def new_category(request):
    form = CategoryForm()
    
    return render(request, 'categories/new.html', {'form': form})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            Category.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                image=form.cleaned_data['image']
            )
            return render(request, 'categories/show.html', {'category': Category.objects.latest('id')})
    else:
        form = CategoryForm()
    
    return render(request, 'categories/new.html', {'form': form})

def show_category(request, category_id):
    category = Category.objects.get(id=category_id)
    
    return render(request, 'categories/show.html', {'category': category})
