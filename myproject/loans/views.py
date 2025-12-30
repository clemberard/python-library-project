from django.shortcuts import render
from .forms import LoanForm
from .models import Loan, Book

# Create your views here.

def loans_view(request):
    """_summary_
    Docstring pour loans_view

    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        Rendered HTML page for loans.
    """
    loans = Loan.objects.all()
    total_loans = loans.count()
    active_loans = loans.filter(status='En cours').count()
    returned_loans = loans.filter(status='retourné').count()
    late_loans = loans.filter(status='en_retard').count()
    
    return render(request, 'loans/index.html', {
        'loans': loans,
        'total_loans': total_loans,
        'active_loans': active_loans,
        'returned_loans': returned_loans,
        'late_loans': late_loans
    })

def show_loan(request, loan_id):
    """_summary_
    Docstring pour show_loan

    Args:
        request (HttpRequest): The HTTP request object.
        loan_id (int): The ID of the loan to display.
    
    Returns:
        Rendered HTML page for a specific loan.
    """
    loan = Loan.objects.get(id=loan_id)
    return render(request, 'loans/show.html', {'loan': loan})

def new_loan(request):
    """_summary_
    Docstring pour new_loan

    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        Rendered HTML page for creating a new loan.
    """
    form = LoanForm()
    return render(request, 'loans/new.html', {'form': form})

def create_loan(request):
    """_summary_
    Docstring pour create_loan

    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        Rendered HTML page after creating a new loan.
    """
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            book = Book.objects.get(id=form.cleaned_data['book'].id)
            new_loan = Loan(
                name_loaner=form.cleaned_data['name_loaner'],
                email_loaner=form.cleaned_data['email_loaner'],
                library_card_number=form.cleaned_data['library_card_number'],
                return_date=form.cleaned_data['return_date'],
                status=form.cleaned_data['status'],
                commentary_librarian=form.cleaned_data['commentary_librarian'],
                book=book
            )
            new_loan.save()
            return render(request, 'loans/show.html', {'loan': new_loan})
    else:
        form = LoanForm()
        return render(request, 'loans/new.html', {'form': form})
    
def edit_loan(request, loan_id):
    """_summary_
    Docstring pour edit_loan

    Args:
        request (HttpRequest): The HTTP request object.
        loan_id (int): The ID of the loan to edit.
    
    Returns:
        Rendered HTML page for editing a specific loan.
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
    """_summary_
    Docstring pour update_loan

    Args:
        request (HttpRequest): The HTTP request object.
        loan_id (int): The ID of the loan to update.
    
    Returns:
        Rendered HTML page after updating a specific loan.
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
    """_summary_
    Docstring pour delete_loan

    Args:
        request (HttpRequest): The HTTP request object.
        loan_id (int): The ID of the loan to delete.
    
    Returns:
        Rendered HTML page after deleting a specific loan.
    """
    loan = Loan.objects.get(id=loan_id)
    loan.delete()
    return render(request, 'loans/index.html')
