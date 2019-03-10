from django import template

register = template.Library()

from ..models import AreaOfInterest


@register.filter
def remove_spaces(value):
    return value.replace(' ', '+')