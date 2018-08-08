from django import template     #因为要应用到前端模板语言，必须导入template
from django.utils.safestring import mark_safe

register = template.Library()   #register的名字是固定的,不可改变


@register.filter
def filter_multi(v1,v2):
    return  v1 * v2
