from django.shortcuts import render,redirect
from .models import eZy_users
from django.contrib import messages

def loginPage(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        users = eZy_users.objects.all()
        user = users.filter(uname=username1,password=password1)
        if user.exists():
            messages.success(request,'You are now logged in as '+user[0].fname)
            return redirect('user_index')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    return render(request, 'auth/login.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['username']
        email = request.POST['email']
        phone =int( request.POST['phone'])
        age = int(request.POST['age'])
        gender = request.POST['genderOptions']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        address = request.POST.get('address')
        if(password == confirmPassword):
            print(fname,lname,uname,email,phone,age,gender,password,address)
            user = eZy_users(fname=fname,lname=lname,uname=uname,email=email,phone=phone,age=age,gender=gender,password=password,address=address)
            user.save()
            redirect('login')
        else:
            print('OKokOK')
        print('Register request received')
        return redirect('login')
    return render(request, 'auth/register.html')