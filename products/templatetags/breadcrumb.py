from django import template

register = template.Library()

@register.simple_tag
def breadcrumb_schema():
    return "http://schema.org/BreadcrumbList"
 
 
@register.inclusion_tag('breadcrumb/home.tpl')
def breadcrumb_home(url='/', title=''):
    return {
        'url': url,
        'title': title
    }
 
 
@register.inclusion_tag('breadcrumb/item.tpl')
def breadcrumb_item(url, title, position):
    return {
        'url': url,
        'title': title,
        'position': position
    }
 
 
@register.inclusion_tag('breadcrumb/active.tpl')
def breadcrumb_active(url, title, position):
    return {
        'url': url,
        'title': title,
        'position': position
    }