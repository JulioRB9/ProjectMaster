from django import template
from django.urls import resolve

register = template.Library()

@register.simple_tag(takes_context=True)
def active_class(context, url_name):
    request = context['request']
    try:
        # Verifica si el nombre de la URL coincide con la actual
        match = resolve(request.path_info)
        if match.url_name == url_name:
            return 'active'
    except:
        return ''
    return ''