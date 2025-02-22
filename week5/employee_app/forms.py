from django import forms
from .models import Employee

class PromotionForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(), label="Employee ID")
    date_of_joining = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Date of Joining")
