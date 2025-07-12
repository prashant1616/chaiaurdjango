from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello world you are at chai aur django")
    return render(request,'website/index.html')
    
def about(request):
    return HttpResponse("hello world you are at about page chai aur django")

def contact(request):
    return HttpResponse("hello world you are at contact page chai aur django")