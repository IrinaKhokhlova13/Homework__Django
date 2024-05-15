from django import template

register = template.Library()

@register.filter()
def media_filter(path):
    if path:
        return f'http://127.0.0.1:8000/media/{path}'
    return "#"