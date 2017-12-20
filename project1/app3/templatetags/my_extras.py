from django import template 

register = template.Library()

@register.filter(name='cut') #decorator sama aja kaya yang baling bawah tentang filter
def cut(value, arg):
	""" ini memmotong semau value dari string """
	return value.replace(arg,'') #python string operation

# register.filter('cut', cut)