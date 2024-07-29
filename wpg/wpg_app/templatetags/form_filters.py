# myapp/templatetags/form_filters.py
from django import template

register = template.Library()

@register.filter
def my_custom_filter(value):
    # Your custom filter logic here
    return value.upper()
# myapp/templatetags/form_filters.py
from django import template

register = template.Library()

@register.filter(name='uppercase')
def uppercase(value):
    """Convert a string to uppercase."""
    return value.upper()
