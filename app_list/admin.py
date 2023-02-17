from django.contrib import admin

from app_list.models import Task, Tag

admin.site.register(Task)
admin.site.register(Tag)
