from django.contrib import admin
from .models import Movie, Rating

# Register your models here.
class MoiveAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created_at', 'updated_at', 'user_id',)

admin.site.register(Movie,MoiveAdmin)