from django import template

register = template.Library()

@register.filter
def rep(s):
    return s.replace(' ','_')
