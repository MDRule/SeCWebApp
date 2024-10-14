from django.contrib import admin

# Register your models here.
#from django.contrib import admin
from .models import Dog


class DogAdmin(admin.ModelAdmin):

    list_display = ('name', 'age', 'breed', 'owner')
    search_fields = ('name', 'breed')
    list_filter = ('age', 'breed', 'owner')
    list_display_links = ('name',)
    fields = ('owner', 'name', 'age', 'breed')

# Register the model and admin class
admin.site.register(Dog, DogAdmin)