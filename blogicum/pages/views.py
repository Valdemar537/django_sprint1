from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'pages/about.html')


def rules(request: HttpRequest) -> HttpResponse:
    return render(request, 'pages/rules.html')
