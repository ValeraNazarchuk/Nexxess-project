from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from .views import *

app_name = 'authentication'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='account_logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)