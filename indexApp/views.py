from django.shortcuts import render
from django.https import HttpResponse

def index(request):
    return HttpResponse(request,'Hello World')
    #return render(request, 'home/index.html')
def about(request):
    return render(request, 'home/about.html')
def contact(request):
    return render(request, 'home/contact.html')
def services(request):
    return render(request, 'home/services.html')
