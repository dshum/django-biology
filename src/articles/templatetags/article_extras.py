from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def page_link(context, page: int = 1):
    request = context['request']
    temp_get = request.GET.copy()
    temp_get['page'] = page
    return '?' + '&'.join([f"{key}={value}" for key, value in temp_get.items()])


@register.filter
def ru_plural(value: int, variants: str):
    value = abs(value)
    variants = variants.split(',')

    if value % 10 == 1 and value % 100 != 11:
        variant = 0
    elif 2 <= value % 10 <= 4 and (value % 100 < 10 or value % 100 >= 20):
        variant = 1
    else:
        variant = 2

    return variants[variant]
