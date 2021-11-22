from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Comment)

class RestaurantAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'tag_list', 'total_rating',)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())
