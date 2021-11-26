from django import template

register = template.Library()

@register.filter


def index(i, j):
    print("soy i",i)
    print("soy j",j)
    return 100