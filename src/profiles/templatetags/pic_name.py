from django import template

register= template.Library()

@register.filter
def pic_name(value):
	name=value.split('/')[-1]
	return name
