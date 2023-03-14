from django import template

register = template.Library()

@register.filter
def in_reserved(things, category):
    return things.filter(seat=category)

@register.filter
def get_at_index(object_list, index):
    print(object_list)
    return object_list[index-1]

@register.filter
def get_item(dictionary, key):
    return dictionary.items.get(key)

@register.filter
def dictionalize(dic):
    return dict(dic)