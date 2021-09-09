from django.contrib import admin
from .models import student

# Register your models here.
class students(admin.ModelAdmin):
    list_display=('name','email')
    search_fields=('name','email',)

admin.site.register(student,students)