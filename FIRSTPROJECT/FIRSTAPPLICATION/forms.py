from django import forms
from .models import Book, Customer, Employee


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields ='__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields ='__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields ='__all__'