from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag
def get_class_name(field, request):
    if request.method == 'GET':
        return "form-control"
    if field.errors:
        return "form-control is-invalid"
    else:
        return "form-control is-valid"
