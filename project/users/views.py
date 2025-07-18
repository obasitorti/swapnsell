from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout
from .forms import CreateUserForm

def logout_view(request):

    django_logout(request)
    return redirect('swapandsell:index')

def register_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = CreateUserForm()
    
    return render(request, 'registration/register.html', {'form': form})
