from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request,'hello.html')
def welcome(request):
    return render(request,'welcome.html')
def hai(request):
    return render(request,'hai.html')