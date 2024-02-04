from django.shortcuts import redirect, render
from django.http.response import HttpResponse


def base(request):
    return render(request, 'core/base.html', {})

def home(request):
    return render(request, 'core/index.html', {})