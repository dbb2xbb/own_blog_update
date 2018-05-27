from django.contrib import admin
from . import models
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','create_time']

class TagAdmin(admin.ModelAdmin):
    list_display = ['tag_name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cate_name']

admin.site.register(models.Post, BlogAdmin)
admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Tag,TagAdmin)
