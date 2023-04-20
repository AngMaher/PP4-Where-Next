from django.contrib import admin
from .models import List
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# admin.site.register(List)

@admin.register(List)
class ListAdmin(SummernoteModelAdmin):

    search_fields = ['title', 'planning']
    summernote_fields = ('planning',)
