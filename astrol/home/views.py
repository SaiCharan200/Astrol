from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Feedback, Login, User, Traits, Rashi
from django.contrib import messages
from .forms import ReportForm
from django.http import HttpResponseRedirect
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        login = Login(username=username, password=password)
        login.save()
        messages.success(request, 'Logged in successfully')

    return render(request, 'website.html')


def register(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        middlename = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email already exists')
            return redirect('register')
        else:
            user = User(firstname=firstname, middlename=middlename, lastname=lastname, email=email, password=password)
            user.save()
            messages.success(request, 'User has been registered successfully!')
            return redirect('login')
    return render(request, 'register.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def freereports(request):
    return render(request, 'freereports.html')


def learnastro(request):
    return render(request, 'learnastro.html')


def numerology(request):
    return render(request, 'numerology.html')


def Birthdate(request):
    return render(request, 'Birthdate.html')


def Numerologynumbers(request):
    return render(request, 'Numerologynumbers.html')


def career(request):
    return render(request, 'career.html')


def feedback(request):
    if request.method == "POST":
        name = request.POST.get('name')
        city = request.POST.get('city')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        feedback = Feedback(name=name, city=city, email=email, phone=phone, desc=desc)
        feedback.save()
        messages.success(request, 'Feedback has been sent')
    return render(request, 'feedback.html')


def Report(request):
    form = ReportForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Your Data has been taken!")
        return HttpResponseRedirect('trait')
    context = {
        "form": form
    }
    return render(request, "Report.html", context)


def trait(request):
    stud = Traits.objects.all()
    print("Myoutput", stud)
    return render(request, 'trait.html', {'stu': stud})


def rashi(request):
    ras = Rashi.objects.all()
    print("Myoutput", ras)
    return render(request, 'rashi.html', {'ras': ras})
