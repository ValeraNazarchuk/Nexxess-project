from django.contrib import admin
from .models import *


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')
    search_fields = ('user', 'avatar')
    list_filter = ('user', 'avatar')
    ordering = ('user', 'avatar')


