from django.shortcuts import render

# Create your views here.

def home1(request):

    return render(request, 'core/home.html')

def about1(request):

    return render(request, 'core/about.html')

def politica1(request):

    return render(request, 'core/politica.html')
