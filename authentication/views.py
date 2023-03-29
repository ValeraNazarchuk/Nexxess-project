from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from io import BytesIO
from .models import *
from .forms import *

def base(request):
    return render(request, "base.html")


def index(request):
    return render(request, "index.html")


def login_view(request):
    if request.method == 'POST':
        login_form = CustomLoginForm(request.POST)
        if login_form.is_valid():
            return redirect('/')
    else:
        login_form = CustomLoginForm()
    context = {'login_form': login_form}

    return render(request, 'authentication.html', context)
