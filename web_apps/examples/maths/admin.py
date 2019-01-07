from django.contrib import admin

from .models import Math

# Register your models here.

class AdminMath(admin.ModelAdmin):
    list_display = ["calculate", "a", "b", "c", "created"]
    list_filter = ["calculate"]
    search_fields = ["c"]


admin.site.register(Math, AdminMath)