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
    
from .models import EzySurveys

def userHome(request):
    user = request.user
    try:
        user = UserModel.objects.get(username=user.username)
    except:
        user = None
        return HttpResponse("You are not logged in, Please login first <a href=\"{% url 'loginPage'%}\">Login</a> first.")
    if user is not None:
        owner = UserModel.objects.filter(username=user.username).first().id
        surveys = EzySurveys.objects.filter(createdBy_id=owner)
        if surveys is not None:
            return render(request,'userHome.html',{'surveys':surveys})
        return render(request,'userHome.html')
    else:
        return HttpResponse("You are not logged in, Please login first ")

def createSurvey(request):
    if request.method == 'POST':
        surveyTitle = request.POST.get('surveyTitle')
        surveyDesc = request.POST.get('surveyDesc')
        user = request.user.username
        owner = UserModel.objects.get(username=user)
        if owner is not None:
            survey = EzySurveys(title=surveyTitle,description=surveyDesc,createdBy=owner,status=True)
            survey.save()
            print(surveyTitle,surveyDesc,owner)
        else:
            print('User not found')
        return redirect('userHome')
    else:
        return render(request,'createSurvey.html')

from .models import EzySurveyQuestions
def addQuestions(request,surveyID):
    survey = EzySurveys.objects.get(surveyID=1)
    if request.method == 'POST':
        qText = request.POST.get('qText')
        qType = request.GET.get('qType') or request.POST.get('qType')
        question = EzySurveyQuestions(surveyID=survey,question=qText,q_type=qType)
        question.save()
        messages.info(request, 'Question added successfully')
        return redirect('addQuestions',surveyID=survey.surveyID)
    else:
        return render(request,'addQuestions.html',{"survey":survey})

def closeSurvey(request,surveyID):
    return HttpResponse('Closed')
def viewResponses(request,surveyID):
    return HttpResponse("Page under construction")
def shareSurvey(request,surveyID):
    return HttpResponse("Page under construction")
def reviewSurvey(request,surveyID):
    survey = EzySurveys.objects.get(surveyID=1)
    questions = EzySurveyQuestions.objects.filter(surveyID=survey)
    return HttpResponse(f"Page under construction {questions[1].q_options} ")

from .models import EzyResponses
def fillSurvey(request,surveyID):
    survey = EzySurveys.objects.get(surveyID=surveyID)
    question = EzySurveyQuestions.objects.get(questionID=1,surveyID=survey)
    response = EzyResponses(questionID=question,response_text="Gowtham")
    response.save()
    if response is not None:
        return HttpResponse(f"Response is {response.response_text}")
    else:
        return HttpResponse("Error in adding response")
    # return render(request,'fillSurvey.html')
def nonUserHome(request):
    return render(request,'nonUserView.html')
def surveyResults(request):
    return render(request,'surveyResultsPage.html')