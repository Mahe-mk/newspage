from django.contrib import admin
from .models import Categories,News,UsersFavoriteCategory
# Register your models here.

admin.site.register(Categories)

class AdminNews(admin.ModelAdmin):
    list_display=('title','category')

admin.site.register(News,AdminNews)
admin.site.register(UsersFavoriteCategory)