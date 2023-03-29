from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views

app_name = 'authentication'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
