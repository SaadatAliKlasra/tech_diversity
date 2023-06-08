from django import template
from django.core.paginator import Paginator

register = template.Library()


@register.simple_tag
def get_proper_elided_page_range(p, number, on_each_side=3, on_ends=2):
    paginator = Paginator(p.object_list, p.per_page)
    return paginator.get_elided_page_range(number=number, on_each_side=on_each_side, on_ends=on_ends)


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    d = context["request"].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()
