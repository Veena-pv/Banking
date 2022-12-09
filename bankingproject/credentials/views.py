from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from banking.models import District,Branch

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print("user created")
                return redirect('login')
        else:
            print("Password not matching")
            messages.info(request, "Password not matching")
            return redirect('register')
    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, "Successfully logged in")
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def regform(request):
    district = District.objects.all()
    branch = Branch.objects.all().filter(district=district)
    return render (request, "regform.html", {'district':district, 'branch':branch})

