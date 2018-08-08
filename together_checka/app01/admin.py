from django.contrib import admin
from app01 import models
# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display = ("title","summary",
                    "img","href","create_date","types","level")


admin.site.register(models.Types)
admin.site.register(models.Level)
admin.site.register(models.Video,VideoAdmin)