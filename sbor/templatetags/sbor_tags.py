from django import template
from sbor.models import *

register = template.Library()

@register.simple_tag()
def get_categories(filter=None):
	if not filter:
		return Category.objects.all()
	else:
		return Category.objects.filter(pk=filter)

@register.inclusion_tag('sbor/list_categories.html')
def show_categories(sort=None, cat_selected=0):
	if not sort:
		cat = Category.objects.all()
	else:
		cat = Category.objects.order_by(sort)
 
	return {"cat": cat, "cat_selected": cat_selected}

