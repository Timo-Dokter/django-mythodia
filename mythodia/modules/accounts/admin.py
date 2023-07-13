from django.contrib import admin

from .models import Account
from .forms import *


# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    add_form = AccountCreationForm
    form = AccountChangeForm
    list_display = ["email", "__str__", "is_dm", "is_staff", "is_active"]
    list_filter = ["is_staff", "is_active", "groups"]
    fieldsets = [
        (
            "Account details",
            {"fields": ("email", "password", "first_name", "last_name")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_dm",
                    "is_active",
                    "is_staff",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ("wide"),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_dm",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    ]
    search_fields = ["email", "first_name", "last_name"]
    ordering = ["email"]
