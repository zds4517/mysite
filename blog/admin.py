from django.contrib import admin

from .models import BlogType,Blog
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name','id')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'blog_type', 'get_read_num', 'author', 'created_time','last_updated_time')
