from django import template
from posts.models import *


register = template.Library()
@register.simple_tag(name = 'get_cats')
def get_categories (filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag(filename = 'posts/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all ()
    else:
        cats = Category.objects.order_by(sort)
    
    return {"cats": cats, "cat_selected": cat_selected}

# @register.inclusion_tag(filename = 'posts/main_menu.html')
# def main_menu():
#     menu = [{'title': "О сайте", 'url_name': 'posts:about'},
#         {'title': "Добавить статью", 'url_name': 'posts:add_page'},
#         {'title': "Обратная связь", 'url_name': 'posts:contact'},
#         {'title': "Войти", 'url_name': 'posts:login'}
#         ]
#     return {'menu':menu}