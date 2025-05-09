from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, PredictionForm  # Add PredictionForm here
from django.contrib.auth.forms import AuthenticationForm
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import json

def home(request):
    return render(request, 'pages/home.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('pages:home')
        messages.error(request, "Registration failed. Please check your input.")
    else:
        form = UserRegistrationForm()
    return render(request, 'pages/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('pages:home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'pages/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('pages:home')
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import json

@login_required
def dashboard(request):
    # Sample statistics
    stats = {
        'total_predictions': 100,
        'approval_rate': 75.5,  # Already as percentage
        'average_confidence': 0.85
    }
    
    # Model metrics (as percentages)
    model_metrics = {
        'accuracy': 85.5,      # 0.855 * 100
        'precision': 82.3,     # 0.823 * 100
        'recall': 78.9,        # 0.789 * 100
        'f1_score': 80.5       # 0.805 * 100
    }
    
    return render(request, 'pages/dashboard.html', {
        'stats': stats,
        'model_metrics': model_metrics,
    })

@login_required
def predict(request):
    result = None
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Get form data
            credit_score = form.cleaned_data['credit_score']
            geography = form.cleaned_data['geography']
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            tenure = form.cleaned_data['tenure']
            balance = float(form.cleaned_data['balance'])
            num_of_products = form.cleaned_data['num_of_products']
            has_credit_card = int(form.cleaned_data['has_credit_card'])
            is_active_member = int(form.cleaned_data['is_active_member'])
            estimated_salary = float(form.cleaned_data['estimated_salary'])
            
            # Create feature array (you'll need to match this with your trained model's expectations)
            features = np.array([
                credit_score,
                1 if geography == 'France' else (2 if geography == 'Spain' else 0),  # One-hot encoding
                1 if gender == 'Male' else 0,  # Binary encoding
                age,
                tenure,
                balance,
                num_of_products,
                has_credit_card,
                is_active_member,
                estimated_salary
            ]).reshape(1, -1)
            
            # For demonstration (replace with your actual model prediction)
            probability = 0.75 if credit_score > 600 and is_active_member == 1 else 0.25
            prediction = 'Low Risk' if probability < 0.5 else 'High Risk'
            confidence = 'High' if abs(probability - 0.5) > 0.3 else 'Medium'
            
            result = {
                'probability': probability * 100,  # Convert to percentage
                'prediction': prediction,
                'confidence': confidence
            }
    else:
        form = PredictionForm()
    
    return render(request, 'pages/predict.html', {
        'form': form,
        'result': result
    })