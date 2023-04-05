from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from .models import *
from .forms import *
from allauth.account.views import SignupView

def main(request):
    if not request.user.is_authenticated:
        return redirect("/accounts/login/")
    else:
        return render(request, "main.html")


def logout_view(request):
    return render(request, 'logout.html')


def login_view(request):
    login_form = CustomLoginForm(request.POST)
    if login_form.is_valid():
        return redirect('/admin ')
    else:
        login_form = CustomLoginForm()
    context = {'login_form': CustomLoginForm}
    return render(request, 'login.html', context)


class CustomSignupView(SignupView):
    form_class = CustomSignupForm
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


def invoices(request):
    return render(request, "invoices.html")


def support(request):
    return render(request, "support.html")


def services(request):
    return render(request, "services.html")