from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PredictionForm(forms.Form):
    credit_score = forms.IntegerField(
        min_value=300,
        max_value=900,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter credit score (300-900)'})
    )
    
    geography = forms.ChoiceField(
        choices=[('France', 'France'), ('Spain', 'Spain'), ('Germany', 'Germany')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    gender = forms.ChoiceField(
        choices=[('Male', 'Male'), ('Female', 'Female')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    age = forms.IntegerField(
        min_value=18,
        max_value=100,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'})
    )
    
    tenure = forms.IntegerField(
        min_value=0,
        max_value=10,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Years as customer (0-10)'})
    )
    
    balance = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Account balance'})
    )
    
    num_of_products = forms.IntegerField(
        min_value=1,
        max_value=4,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of products (1-4)'})
    )
    
    has_credit_card = forms.ChoiceField(
        choices=[(1, 'Yes'), (0, 'No')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    is_active_member = forms.ChoiceField(
        choices=[(1, 'Yes'), (0, 'No')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    estimated_salary = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Estimated salary'})
    )