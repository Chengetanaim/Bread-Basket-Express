from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method != 'POST':
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('products:index')
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'registration/logged_out.html')
    