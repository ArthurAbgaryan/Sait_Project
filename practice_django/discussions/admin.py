
from django.contrib import admin
from .models import Discussion

@admin.register(Discussion)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title',]
    prepopulated_fields = {'slug':('title',)}

# Register your models here
