from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseRedirect
from io import BytesIO
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.views.generic import TemplateView
from allauth.account.views import LogoutView
from allauth.account.views import LogoutView
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
# from .forms import SignupForm
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.encoding import force_bytes, force_text
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.template.loader import render_to_string
# from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from django.shortcuts import redirect

def custom_login_failed_page(request):
    return redirect('/custom-login-page/')

# class HomePageView(TemplateView):
#     template_name = 'index.html'
def base(request):
    return render(request, "base.html")


def index(request):
    return render(request, "index.html")


def logout_view(request):
    return render(request, 'logout.html')


def login_view(request):
    if request.method == 'POST':
        pass
    else:
        login_form = CustomLoginForm()
    context = {'login_form': CustomLoginForm}
    return render(request, 'login.html', context)

                         # login_form = CustomLoginForm(request.POST)
        # if login_form.is_valid():
        #     return redirect('/admin')
            # name = login_form.cleaned_data['username']
            # # login_form = CustomLoginForm(request.POST)
            # return HttpResponse(f'Welcome {name}')
        # if login_form.is_valid():
        #     username = login_form.cleaned_data['username']
        #     password = login_form.cleaned_data['password']
        #     user = authenticate(username=username, password=password)
        #     if user is not None:
        #         login(request, user)
        #         return redirect('/')
        # else:
        #     return HttpResponse('Invalid login credentials')
        #             # messages.error(request, 'Invalid login credentials')



# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             # save form in the memory not in database
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             # to get the domain of the current site
#             current_site = get_current_site(request)
#             mail_subject = 'Activation link has been sent to your email id'
#             message = render_to_string('acc_active_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid':urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token':account_activation_token.make_token(user),
#             })
#             to_email = form.cleaned_data.get('email')
#             email = EmailMessage(
#                         mail_subject, message, to=[to_email]
#             )
#             email.send()
#             return HttpResponse('Please confirm your email address to complete the registration')
#     else:
#         form = SignupForm()
#     return render(request, 'signup.html', {'form': form})

# def activate(request, uidb64, token):
#     User = get_user_model()
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
#     else:
#         return HttpResponse('Activation link is invalid!')
#
