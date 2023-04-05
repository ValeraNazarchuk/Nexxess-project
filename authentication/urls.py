from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from authentication.views import *

app_name = 'authentication'

urlpatterns = [
    path('', main, name='main'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='account_logout'),
    path('invoices/', invoices, name='invoices'),
    path('support/', support, name='support'),
    path('services/', services, name='services'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)