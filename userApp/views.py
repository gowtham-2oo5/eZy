from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import user_forms,form_questions,form_answers
from authApp.models import eZy_users
# Create your views here.
def index(request):
    return render(request, 'user/index.html')
# currentUser = eZy_users()
def create_form(request):
    if request.method == 'POST':
        return HttpResponse('Post being created by '+ currentUser.uname )
    return render(request,'user/create_form.html')
currentForm = user_forms()
def add_questions(request):
    if request.method == 'POST':
        question = request.POST['question_text']
        questionType = request.POST['qType']
        mandatory = request.POST['mandatory']
        print(question,questionType,mandatory)
        messages.success(request, 'Question added successfully')
        print(currentForm.form_id)
        newQuestion = form_questions(question_text=question,
                                     question_type=questionType,
                                     question_required=mandatory=='on',
                                     form_id=user_forms.objects.filter(form_id=currentForm.form_id).first())
        newQuestion.save()        
        return redirect('add_questions')
    else:
        return render(request,'user/add_questions.html')
def save_user(request):
    if request.method == 'POST':
        uname = request.POST['username'][25:]
        user = eZy_users.objects.all().filter(fname=uname)
        print(user[0].uname)
        createUser(user[0])
        return redirect('refresh_user')
def createUser(user):
    global currentUser
    currentUser = user
    currentUser.save()
    print(currentUser.uname)

def refresh_user(request):
        return render(request,'user/index.html', {'ezy_user':currentUser})
    
def manage_forms(request):
    return render(request,'user/manage_forms.html')

def manage_profile(request):
    uid = currentUser.id
    user = eZy_users.objects.get(id=uid)
    print(user.fname)
    return render(request,'user/manage_profile.html',{'user':user})

def logout(request):
    currentUser = eZy_users()
    return redirect('home')
from .models import grievances
def user_grievances(request):
    if request.method == 'POST':
        uname = request.POST['name']
        issue = request.POST['issue']
        message = request.POST.get['message']
        g = grievances(grievance_user=uname,grievance_issue = issue,grievance_message=message)
        g.save()
        messages.success(request, 'Grievance submitted successfully')
        return redirect('user_grievances')
    return render(request,'user/user_grievances.html')

from django.contrib import messages
def update_profile(request):
    if request.method == 'POST':
        password = request.POST['password']
        cpwd = request.POST['confirmPassword']
        if password != cpwd:
            messages.error(request, 'Password does not match')
            redirect('manage_profile')
        else:
            uid = currentUser.id
            user = eZy_users.objects.get(id=uid)
            user.uname = request.POST['username']
            user.fname = request.POST['fname']
            user.lname = request.POST['lname']
            user.email = request.POST['email']
            user.phone = request.POST['phone']
            user.age = request.POST['age']
            user.password = request.POST['password']
            user.address=request.POST.get['address']
            user.save()
            createUser(user)
            return redirect('refresh_user')
    return render(request,'user/manage_profile.html')

import datetime

def initialize_form(request):
  user = currentUser
  if request.method == 'POST':
    form_title = request.POST['form_title']
    form_desc = request.POST['form_desc']
    currTime = datetime.datetime.now() 
    form = user_forms(form_name=form_title,
                      form_desc=form_desc,
                      form_owner=user.id,
                      form_created=currTime,
                      form_updated=currTime,
                      form_status=True)
    form.save()
    global currentForm
    currentForm = form
    currentForm.save()
    return redirect('add_questions')
  else:
    return render(request, 'user/create_form.html')
