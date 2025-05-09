# Customer Churn Prediction Platform

A web-based platform that predicts customer churn probability using machine learning, built with Django and Bootstrap.

## Project Overview

This application helps businesses predict customer churn by analyzing various customer attributes such as credit score, age, tenure, and banking behavior. It provides an intuitive interface for making predictions and visualizing results.

## Dataset Description

The model is trained on a banking customer dataset with the following features:
- Credit Score (300-900)
- Geography (France, Spain, Germany)
- Gender (Male, Female)
- Age (18-100)
- Tenure (0-10 years)
- Balance
- Number of Products (1-4)
- Has Credit Card (Yes/No)
- Is Active Member (Yes/No)
- Estimated Salary

## Model Training Process

1. Data Preprocessing
   - Handling missing values
   - Feature scaling
   - Encoding categorical variables (Geography, Gender)
   - Train-test split (80-20)

2. Model Development
   - Algorithm selection based on performance metrics
   - Hyperparameter tuning
   - Cross-validation
   - Model evaluation using accuracy, precision, recall, and F1-score

## Authentication Implementation

The application implements Django's built-in authentication system with custom styling:

1. User Registration
   - Email verification
   - Password validation
   - Custom user registration form

2. Login/Logout System
   - Session management
   - Secure password handling
   - Protected routes using @login_required decorator


## Challenges Encountered

1.Data Preprocessing Challenges
- Handling imbalanced dataset for churn prediction
- Converting categorical variables (Geography, Gender) into numerical format
- Normalizing numerical features with different scales
- Dealing with outliers in Balance and Estimated Salary fields

## Integration Steps

1. Django Setup
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver