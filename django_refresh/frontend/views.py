from django.shortcuts import render

def index(requests):
    return render(request, 'frontend/index.html')