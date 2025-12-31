from django.shortcuts import render
from .forms import LoanForm
from .models import Loan, Book

# Create your views here.

def loans_view(request):
    """
    Affiche la liste de tous les prêts.
    """
    loans = Loan.objects.all()
    total_loans = loans.count()
    active_loans = loans.filter(status='en_cours').count()
    returned_loans = loans.filter(status='retourne').count()
    late_loans = loans.filter(status='en_retard').count()
    
    return render(request, 'loans/index.html', {
        'loans': loans,
        'total_loans': total_loans,
        'active_loans': active_loans,
        'returned_loans': returned_loans,
        'late_loans': late_loans
    })

def show_loan(request, loan_id):
    """
    Affiche les détails d'un prêt spécifique.
    """
    loan = Loan.objects.get(id=loan_id)
    return render(request, 'loans/show.html', {'loan': loan})

def new_loan(request):
    """
    Affiche le formulaire pour créer un nouveau prêt.
    """
    if request.GET.get('book'):
        form = LoanForm(initial={'book': request.GET.get('book')})
    else:
        form = LoanForm()
    return render(request, 'loans/new.html', {'form': form})

def create_loan(request):
    """
    Traite le formulaire de création d'un nouveau prêt.
    """
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            new_loan = form.save()
            decrement_book(new_loan.book.id)
            return render(request, 'loans/show.html', {'loan': new_loan})
        else:
            return render(request, 'loans/new.html', {'form': form})
    else:
        form = LoanForm()
        return render(request, 'loans/new.html', {'form': form})
    
def edit_loan(request, loan_id):
    """
    Affiche le formulaire pour éditer un prêt existant.
    """
    loan = Loan.objects.get(id=loan_id)
    form = LoanForm(initial={
        'name_loaner': loan.name_loaner,
        'email_loaner': loan.email_loaner,
        'library_card_number': loan.library_card_number,
        'return_date': loan.return_date,
        'status': loan.status,
        'commentary_librarian': loan.commentary_librarian,
        'book': loan.book
    })
    return render(request, 'loans/edit.html', {'form': form, 'loan': loan})

def update_loan(request, loan_id):
    """
    Traite le formulaire de mise à jour d'un prêt existant.
    """
    loan = Loan.objects.get(id=loan_id)
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            loan.name_loaner = form.cleaned_data['name_loaner']
            loan.email_loaner = form.cleaned_data['email_loaner']
            loan.library_card_number = form.cleaned_data['library_card_number']
            loan.return_date = form.cleaned_data['return_date']
            loan.status = form.cleaned_data['status']
            loan.commentary_librarian = form.cleaned_data['commentary_librarian']
            loan.book = Book.objects.get(id=form.cleaned_data['book'].id)
            loan.save()
            return render(request, 'loans/show.html', {'loan': loan})
    else:
        form = LoanForm(initial={
            'name_loaner': loan.name_loaner,
            'email_loaner': loan.email_loaner,
            'library_card_number': loan.library_card_number,
            'return_date': loan.return_date,
            'status': loan.status,
            'commentary_librarian': loan.commentary_librarian,
            'book': loan.book
        })
    return render(request, 'loans/edit.html', {'form': form, 'loan': loan})

def delete_loan(request, loan_id):
    """
    Supprime un prêt spécifique.
    """
    loan = Loan.objects.get(id=loan_id)
    loan.delete()
    
    loans = Loan.objects.all()
    total_loans = loans.count()
    active_loans = loans.filter(status='en_cours').count()
    returned_loans = loans.filter(status='retourne').count()
    late_loans = loans.filter(status='en_retard').count()
    
    return render(request, 'loans/index.html', {
        'loans': loans,
        'total_loans': total_loans,
        'active_loans': active_loans,
        'returned_loans': returned_loans,
        'late_loans': late_loans
    })

def return_loan(request, loan_id):
    """
    Traite le retour d'un prêt
    """
    loan = Loan.objects.get(id=loan_id)
    loan.status = 'retourne'
    loan.save()
    return render(request, 'loans/show.html', {'loan': loan})

def decrement_book(book_id):
    book = Book.objects.get(id=book_id)
    if (book.copies_available > 0):
        book.copies_available -= 1
        book.save()