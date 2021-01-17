from django.shortcuts import render
from django.http import HttpResponse
from app.forms import LoginForm


def index(request):
    context = {'form' : LoginForm()}
    return render(request, 'app/index.html', context)

