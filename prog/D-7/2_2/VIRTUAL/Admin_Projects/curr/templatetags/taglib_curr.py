from django import template

register = template.Library()

@register.simple_tag
# def print(param):
def p(param):
# def show(param):
    
    param = param + " done"
    
#     return "yes : " % (param)
#     return "yes : " % param
    return param


#ref https://stackoverflow.com/questions/4731572/django-counter-in-loop-to-index-list
@register.filter
def access_index(sequence, position):
    return sequence[position]

# @register.simple_tag

# @register.tag
@register.simple_tag
def get_CurrencyPair_Name(param):
    
    tokens = param.split(".")
    
    return tokens[0]
#     return "yes : %s" % param