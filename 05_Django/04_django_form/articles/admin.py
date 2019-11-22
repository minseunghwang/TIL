from django.contrib import admin
from .models import Article, Comment, Hashtag, Mapmap

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk','title','content','created_at','updated_at',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk','content','created_at','updated_at',)

class HashtagAdmin(admin.ModelAdmin):
    list_display = ('content',)

class MapmapAdmin(admin.ModelAdmin):
    list_display = ('road_num','address','xposition')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Hashtag, HashtagAdmin)
admin.site.register(Mapmap, MapmapAdmin)