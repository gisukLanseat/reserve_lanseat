from django.contrib import admin
from .models import reservation

@admin.register(reservation)
class MyAdimn(admin.ModelAdmin):
    list_display = ['seat','date','student']
    list_filter = ['seat','date','student']
    search_fields = ['seat','student']