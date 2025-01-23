from django.contrib import admin
from .models import User


@admin.register(User)
class UserPanel (admin.ModelAdmin) : 
    list_display = ['username','email','full_name']