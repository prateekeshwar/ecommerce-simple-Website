from django.contrib import admin

from .models import UserProfile,Category
# Register your models here.
class UserProfileModelAdmin(admin.ModelAdmin):
    # list_display=["album_title","timestamp","updated"]
    # list_filter=["updated","timestamp"]
    # search_fields=['Name']
    class Meta:
        model = UserProfile
class CategoryModelAdmin(admin.ModelAdmin):
    #list_display=["album_title","timestamp","updated"]
    #list_filter=["updated","timestamp"]
    #search_fields=["album_title","artist"]
    class Meta:
        model = Category
admin.site.register(UserProfile,UserProfileModelAdmin)
admin.site.register(Category,CategoryModelAdmin)