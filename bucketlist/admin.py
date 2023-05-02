from django.contrib import admin
from .models import List
from django_summernote.admin import SummernoteModelAdmin


@admin.register(List)
class ListAdmin(SummernoteModelAdmin):

    search_fields = ['title', 'user_name', 'planning']
    summernote_fields = ('planning',)
    list_filter = ['user_name']
