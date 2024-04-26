from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'hero.html')

def registrationPage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            toDBUser = UserModel(username=user.username, email=user.email, password=user.password)
            toDBUser.save()
            login(request, user)
            return redirect('userHome')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def contactForm(request):
    if request.method == 'POST':
        uMail = request.POST.get('email')
        uTitle = request.POST.get('title')
        uMessage = request.POST.get('message')
        print(uMail,uTitle,uMessage)
    pass

from django.contrib import messages
from .forms import RegisterForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import UserModel

def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('userHome')
            else:
                return HttpResponse("Wrong credentials")
                # form.add_error(None, 'Invalid username or password')
        else:
            pass 
    else:
        form = AuthenticationForm()
    return render(request, 'loginPage.html', {'form': form})

def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
        return HttpResponse('Error in logging out')

def forgotPass(request):
    return render(request,'forgotPass.html')    
    
def userHome(request):
    return render(request,'userHome.html')
def createSurvey(request):
    return render(request,'createSurvey.html')
def fillSurvey(request):
    return render(request,'fillSurvey.html')
def nonUserHome(request):
    return render(request,'nonUserView.html')
def surveyResults(request):
    return render(request,'surveyResultsPage.html')