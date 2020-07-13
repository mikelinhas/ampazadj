# Custom filters for view

from django import template


register = template.Library()


@register.filter(name='wordify')
def wordify(value):
	return value.replace("_", " ").capitalize()
