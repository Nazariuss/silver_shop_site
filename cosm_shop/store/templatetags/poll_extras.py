from django import template

register = template.Library()

@register.filter()
def multiply(v, a):
    return v * a