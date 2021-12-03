from django.shortcuts import render

from django.http import HttpResponse

from  listings.models import Band
# Create your views here.

def hello(request):
    bands = Band.objects.all()
    return render(request,'listings/hello.html', {'bands' : bands} )

def about(request):
    return HttpResponse("<h1>About us </h1>")


def contact(request):
    return HttpResponse("<h1>Contact us </h1>")

def help(request):
    return HttpResponse("<h1>Contact us </h1>")
