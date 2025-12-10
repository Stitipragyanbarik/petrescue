from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import logout
from django.views.decorators.http import require_http_methods
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings

def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                # respect "next" parameter if safe
                next_url = request.POST.get('next') or request.GET.get('next')
                if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={*settings.ALLOWED_HOSTS, '127.0.0.1', 'localhost'}):
                    return redirect(next_url)
                return redirect('home')  # Redirect to a home page or dashboard
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        # Pass the request to AuthenticationForm so it can access request-specific auth data
        form = AuthenticationForm(request)
    # propagate next parameter to template so the form can include it
    next_param = request.GET.get('next', '')
    return render(request, 'accounts/login.html', {'form': form, 'next': next_param})


@require_http_methods(["GET", "POST"])
def logout_view(request):
    """Log out the user, add a message, and redirect to home."""
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')
