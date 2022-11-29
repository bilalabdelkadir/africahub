from django.contrib import admin
from .models import Article, Comment , Vote, Roadmap, Link, Roadmapsubtitle
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_at')
    list_filter = ("status",)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}

class RoadmapAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_at')
    list_filter = ("status",)
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)
admin.site.register(Roadmap, RoadmapAdmin)
admin.site.register(Roadmapsubtitle)
admin.site.register(Link)