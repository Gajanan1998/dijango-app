from django.shortcuts import render, redirect
from django.contrib import messages
import FRM.models as md
from django.db import connection
from datetime import datetime
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        global user
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Fetch the user from the database
        try:
            user = Credentials.objects.get(username=username)
            # Check if the password matches (In production, ensure password hashing)
            if user.password == password:
                # Set the session data request.session['username'] = user.username
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                request.session['is_authenticated'] = True
                print(request.session['username'])
                messages.success(request, f"Welcome {user.username}!")
                return redirect('dashboard')
            # Replace 'home' with your homepage URL name
            else:
                messages.error(request, "Invalid password.")
        except Credentials.DoesNotExist:
            messages.error(request, "Username does not exist.")
            return render(request, 'login.html')
    return render(request, 'login.html')


def dashboard(request):
    context = md.dashboard_model()
    context['username'] = request.session['username']
    print(Credentials)
    return render(request, 'dashboard.html', context)

from django.core.exceptions import ValidationError
from django.core.validators import validate_email


from FRM.models import Credentials
def signup(request):
    if request.method == 'POST':
        # Extract data from POST request
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if username == "" or email == "" or password == "":
            return render(request, 'signup.html')

        credentials = Credentials(username=username, email=email, password=password)
        print(f"----{credentials}----")
        credentials.save()
        return redirect('login')
    # Handle POST request
    return render(request, 'signup.html')

def forgotpassword(request):
    return render(request, 'forgotpassword.html')

def transactionreport(request):
    with connection.cursor() as cursor:
        # Execute a raw SQL query
        cursor.execute("SELECT [txn_id] ,[rule_id] ,[rule_name] FROM [FRM].[dbo].[suspicious_transaction]")
        # Fetch all rows
        rows = cursor.fetchall()

        # Get column names
        columns = [desc[0] for desc in cursor.description]

    # Ensure the context is a dictionary
    context = {
        'rows': rows,
        'columns': columns
    }
    return render(request, 'transactionreport.html', context)

def logout_view(request):
    request.session.flush()
    return redirect('login')

def rules_creation_view(request):
    if request.method == 'POST':
        rule_name = request.POST.get('ruleName')
        rule_details = request.POST.get('ruleDetails')
        rule_desc = request.POST.get('ruleDesc')
        rule_status = request.POST.get('ruleStatus')
        rule_created_date = request.POST.get('ruleCreatedDate')  # Expected format: "MM/DD/YYYY HH:MM AM/PM"
        rule_expiry_date = request.POST.get('ruleExpiryDate')    # Same format
        print(rule_created_date)

        #Validate that all fields are provided
        if not all([rule_name, rule_details, rule_desc, rule_created_date, rule_expiry_date]):
            return render(request, 'rules_creation.html', {'error': 'All fields are required.'})

        try:
            # Create and save the Rule instance
            rule_instance = md.Rule(
                ruleName=rule_name,
                rule_details=rule_details,
                rule_desc=rule_desc,
                rule_status=rule_status,  
                rule_created_date=rule_created_date,
                rule_expiry_date=rule_expiry_date
            )
            rule_instance.save()
            return redirect('dashboard')  # Redirect after saving

        except ValueError:
            print(ValueError)
            return render(request, 'rules_creation.html', {'error': 'Invalid date format. Use MM/DD/YYYY HH:MM AM/PM.'})
        except ValidationError as e:
            print(e)
            return render(request, 'rules_creation.html', {'error': str(e)})

    return render(request, 'rules_creation.html')

def rules_list_view(request):
    with connection.cursor() as cursor:
        # Execute a raw SQL query
        cursor.execute("SELECT * FROM [FRM].[dbo].[Rule]")
        # Fetch all rows
        rows = cursor.fetchall()

        # Get column names
        columns = [desc[0] for desc in cursor.description]

    # Ensure the context is a dictionary
    context = {
        'rows': rows,
        'columns': columns
    }
    return render(request, 'rules_list.html', context)
