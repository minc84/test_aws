from .models import *
from django.db.models import Count
 
menu = [{'title': "О нас", 'url_name': 'about'},
        {'title': "Способы оплаты", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "контакты", 'url_name': 'login'}
]
 
class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('sbor'))
        context['menu'] = menu
        context['cats'] = cats  
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context    