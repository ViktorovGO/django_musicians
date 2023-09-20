from .models import *
from django.db.models import *
from django.core.cache import cache
menu = [{'title': "О сайте", 'url_name': 'posts:about'},
        {'title': "Добавить статью", 'url_name': 'posts:add_page'},
        {'title': "Обратная связь", 'url_name': 'posts:contact'},
        ]

class DataMixin:
    paginate_by = 3
    def get_user_context(self, **kwargs):
            
            context = kwargs
            cats = cache.get('cats')
            if not cats:
                cats = Category.objects.annotate(Count('musician'))
                cache.add('cats', cats, 60)
                
            user_menu = menu.copy ()
            if not self.request.user.is_authenticated:
                user_menu.pop(1)
            context['menu'] = user_menu
            context['cats'] = cats
            if 'cat_selected' not in context:
                  context['cat_selected'] = 0
            return context