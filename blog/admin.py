from django.contrib import admin
from .models import Blog_Category, Blog

admin.site.register(Blog_Category)

@admin.register(Blog)
class ArticleAdmin(admin.ModelAdmin):
    
    list_display = ["title","date","published"]
    list_display_links = ["title","date","published"]
    search_fields = ["title"]
    list_filter = ["date","published"]
    class Meta:
        model = Blog

