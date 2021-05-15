from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['head', 'text', 'pub_date']
    list_filter = ['head', 'pub_date']
    ordering = ['-pub_date']


admin.site.register(News, NewsAdmin)
