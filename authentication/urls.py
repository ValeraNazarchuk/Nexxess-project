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
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#
# from django.urls import path
# from .views import home, index, activate
# urlpatterns = [
# path('', home, name = 'home'),
# path('form/', index, name = 'index'),
# path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
# activate, name='activate'),
# ]