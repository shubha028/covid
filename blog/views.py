from django.shortcuts import render
from django.http import HttpResponseRedirect

def login_page(request):
    return render(request,'account/login.html')
def registration_page(request):
    return render(request,'blog/registration.html')
def appointment_page(request):
    return render(request,'blog/appointment.html')
# Create your views here.
# def home( request):
#     return render(request,'blog/index.html')
