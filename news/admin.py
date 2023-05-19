from django.contrib import admin
from .models import Categories,News,UsersFavoriteCategory,ExtraField
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountInLine(admin.StackedInline):
    model = ExtraField
    verbose_name = "Extra Fields"
class CustomizedUserAdmin(UserAdmin):
    inlines = (AccountInLine,)

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
admin.site.register(Categories)

class AdminNews(admin.ModelAdmin):
    list_display=('title','category')
admin.site.register(News,AdminNews)
admin.site.register(UsersFavoriteCategory)