from django.contrib import admin
from user.models import User
from unfold.admin import ModelAdmin as UnfoldModelAdmin
class UnfoldModelAdmin(UnfoldModelAdmin):
    list_display = ['username', 'email','is_active','role']

admin.site.register(User,UnfoldModelAdmin)