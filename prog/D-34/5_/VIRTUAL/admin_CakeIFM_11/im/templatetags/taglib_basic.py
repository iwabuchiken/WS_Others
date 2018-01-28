from django import template

register = template.Library()

@register.simple_tag
# def print(param):
def p(param):
# def show(param):
    
    return param
