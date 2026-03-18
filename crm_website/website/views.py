from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Record
from .forms import AddRecordForm


# Create your views here.

def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request , ' you have logged in successfully')
            return redirect('home')
        else:
            messages.success(request, 'there was an error logginging')
            return redirect('home')
    else:
        return render(request, 'home.html' , {'records': records })



def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, 'you have logged out')
    return redirect('home')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists try another one')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists try another one')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('home')
        else:
            messages.info(request, 'Password did not matched')    
            return redirect('register')
    else:
        return render(request, 'register.html')        
    

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'record': customer_record})
    else:
            messages.info(request, 'You are not logged in ')    
            return redirect('home')
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.info(request, 'Record deleted successfully...')
        return redirect('home')
    else:
        messages.info(request, 'You must log in first')
        return redirect('home')

    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                new_record = form.save()
                messages.success(request, 'form added successfully....')
                return redirect('home')
        else:
            return render(request, 'add_record.html', {'form': form})
    else:
        messages.info(request, 'you need to login first' )
        return redirect('home')

    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record =  Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your record has been updated')
            return redirect('home')
        return render(request, 'update_record.html', {'form': form })
    else:
        messages.info(request, 'You must be logged update  the record....')        
        return redirect('home')