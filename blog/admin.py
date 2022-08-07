from django.contrib import admin

from .models import Category, Post, Comment

class CommentsInline(admin.TabularInline):
    model = Comment
    raw_id_fields=['post']

class CustomPostAdmin(admin.ModelAdmin):
    search_fields=['title']
    list_display = ["title", 'slug','created_at']
    list_filter = ['title' , 'created_at', 'status']

    prepopulated_fields = {'slug':['title']}

    inlines = [CommentsInline]

# Register your models here.
admin.site.register(Post, CustomPostAdmin)
admin.site.register(Comment)
admin.site.register(Category)