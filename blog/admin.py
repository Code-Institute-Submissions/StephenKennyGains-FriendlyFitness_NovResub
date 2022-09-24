""" Admin.py allows for CRUD functionality for blog posts through
an admin panel and enables approval of user commenting on posts"""

from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Sets the display and functionality for blog posting """

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'content')
