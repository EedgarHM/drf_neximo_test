from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages

from .forms import RegistrationForm

User = get_user_model()

def register_user(request):
    if request.method == 'POST':

        form = RegistrationForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']

            try:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'User already exists')
                else:
                    user = User.objects.create_user(email=email, password=password, name=name)
                    messages.success(request,'User saved correctly')
                    return redirect('registration_success')
                
            except Exception as e:
                return render(request, 'register.html', {'form': form, 'error_message': 'Error registering user'})
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})
