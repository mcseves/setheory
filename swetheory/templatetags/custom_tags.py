from django import template

register = template.Library()


@register.filter
def remove_spaces(value):
    return value.replace(' ', '+')

