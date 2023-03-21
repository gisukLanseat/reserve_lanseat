from django import template

register = template.Library()

@register.filter
def in_reserved(things, category):
    return things.filter(seat=category)

@register.filter
def get_at_index(object_list, index):
    return object_list[index-1]

@register.filter
def get_item(dictionary, key):
    return dictionary[key]

@register.filter
def dictionalize(dic):
    return dict(dic)

@register.filter
def Tolist(t):
    return t.replace("[", "").replace("[", "").split(",")