from django.contrib import admin

from .models import Trash


class TrashAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'trash_type', 'weight',)


admin.site.register(Trash, TrashAdmin)
