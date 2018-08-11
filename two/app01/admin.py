from django.contrib import admin
from app01.models import *
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title",)

    class Media:
        js=(
            "/static/js/kindeditor-4.1.10/kindeditor-all.js",
            "/static/js/kindeditor-4.1.10/lang/zh_CN.js",
            "/static/js/kindeditor-4.1.10/config.js",
        )
admin.site.register(Article,ArticleAdmin)