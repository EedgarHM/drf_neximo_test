from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .forms import RegistrationForm, LoginForm
from app.utils.generate_token import generate_token
from app.utils.validate_token import validate_token

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


def login(request):
    """ Login form """
    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():
                
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            # User autentication
            user = authenticate(request, email=email, password = password)

            if user is not None:

                # Generate JTW if the user is right
                jwt_token = generate_token(user)

                print(f"token de autenticacion {jwt_token}")
                return redirect(f'/api/payments?token={jwt_token}')
            
            else:
                messages.error(request, 'Credentials are not valid')
                form.add_error(None, 'Credentials are not valid')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})



@api_view(['POST'])
def payments(request):

    USD_CURRENCY = 17

    token=''

    authorization_header = request.META.get('HTTP_AUTHORIZATION')
    if authorization_header and authorization_header.startswith('JWT '):
        token = authorization_header[4:]

    if not token:
        messages.error(request, 'Token Required')
        if request.META.get('HTTP_ACCEPT') == '*/*':
            return Response({'Error' :'Token must be sended'})
    else:
        is_token_valid = validate_token(token)

        if not is_token_valid:
            messages.error(request, 'Token is not valid')
            if request.META.get('HTTP_ACCEPT') == '*/*':
                return Response({'Error':'Token no válido','status':status.HTTP_401_UNAUTHORIZED})
            else:
                return Response({'Error':'Token no válido','status':status.HTTP_401_UNAUTHORIZED})

        if request.method == 'POST':

            response = {}
            data = request.data

            total_amount = 0
            taxes = 0
            commission = 0

             # Check if the currency is USD or MXN

            for item in data:
                # Check if the currency is USD or MXN
                if item['currency'] == 'MXN':
                    #check amount
                    if item['amount'] <=500:
                        total_amount+=item['amount'] 
                    else:
                        total_amount = int(item['amount']  / (1 + 0.16) )
                        taxes+= int(total_amount * 0.16)
                else:
                    print("Estamos en el else")
                    # convert the amount and check it
                    total_currency_amount_mx = int(item['amount'] * 17)
                    if total_currency_amount_mx <=500:
                        total_amount+=total_currency_amount_mx
                        commission += total_currency_amount_mx * 1.03
                    else:
                        commission += total_currency_amount_mx * 0.03
                        taxes += total_currency_amount_mx * 0.16
                        total_amount += total_currency_amount_mx * 1.19
            response = {
                "total" : total_amount,
                "taxes" : taxes,
                "commission" : commission
            }
        return Response({'response': response})