from django.contrib import admin
from posts.models import Musician, Category, Comment
from django.utils.safestring import mark_safe

# Register your models here.
class MusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_photo', 'time_update', 'is_published', 'user')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug':('title',)}
    fields = ('title', 'slug', 'cat', 'content','photo','get_html_photo', 'is_published','time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update','get_html_photo')
    save_on_top = True
    def get_html_photo (self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=100>")
    get_html_photo.short_description = 'Миниатюра'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)} 
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content',)
    list_display_links = ('id', 'content',)
    search_fields = ('content',)
admin.site.register(Musician, MusAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment,CommentAdmin)

admin.site.site_header = ('Админ панель сайта о музыкантах')
admin.site.site_title = ('Админ панель сайта о музыкантах')