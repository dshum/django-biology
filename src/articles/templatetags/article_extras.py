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


@register.filter
def filesize(file_size: int, unit: str = 'bytes'):
    exponents_map = {'bytes': 0, 'kb': 1, 'mb': 2, 'gb': 3}
    if unit not in exponents_map:
        raise ValueError('Must select from bytes, kb, mb, gb')
    else:
        size = file_size / 1024 ** exponents_map[unit]
        return round(size)
