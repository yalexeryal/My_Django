from django.template.defaultfilters import stringfilter
from django import template

register = template.Library()


@register.filter(name='split')
@stringfilter
def split(value, key=' '):
    return value.split(key)
