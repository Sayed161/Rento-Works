from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomerSignupForm, LoginForm
from django.contrib.auth import login,authenticate
from .models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        form = CustomerSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            backend = 'Account.authentication.EmailBackend'  # or ''
            user.backend = backend
            
            login(request, user, backend=backend)  
            
            return redirect('home')
             
    else:
        form = CustomerSignupForm()

    return render(request, 'sign_up.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            print('Authentication successful',user)
            if user is not None:
                login(request, user)  # Log the user in
                messages.success(request, "You have successfully logged in!")
                return redirect('home')  # Redirect to the homepage or a specific dashboard
            else:
                messages.error(request, "Invalid email or password. Please try again.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})