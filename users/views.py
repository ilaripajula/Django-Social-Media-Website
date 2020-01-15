from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    #using a pre-made class to convert classes into html files we can create a user
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})

# Create your views here.
