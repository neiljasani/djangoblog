from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# Handles traffic from the homepage
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

# Handles traffic from the about page
def about(request):
    return HttpResponse('<h1>Blog About</h1>')
