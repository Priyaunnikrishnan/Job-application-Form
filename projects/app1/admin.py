from .models import Form
from django.contrib import admin


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("date", "occupation")
    ordering = ("first_name",)
    readonly_fields = ("occupation",)


admin.site.register(Form, FormAdmin)
