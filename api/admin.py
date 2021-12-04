from django.contrib import admin
from django.contrib.admin.decorators import display

from api.models import Experience, Skills

# Register your models here.

class skillModel(admin.ModelAdmin):
    list_display = ('id','name','experience_lvl')

admin.site.register(Skills,skillModel)
admin.site.register(Experience)