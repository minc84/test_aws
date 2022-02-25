from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .utils import *
from django.core.paginator import Paginator
# Create your views here.список menu, указав не только заголовок, но и имя ссылки:

# menu = [{'title': "О сайте", 'url_name': 'about'},
# 	{'title': "Добавить статью", 'url_name': 'add_page'},
# 	{'title': "Обратная связь", 'url_name': 'contact'},
# 	{'title': "Войти", 'url_name': 'login'}
# ]


class SborHome(DataMixin, ListView):
	
	model = Sbor
	template_name = 'sbor/index.html'
	context_object_name = 'posts'
	#extra_context = {'title': 'Главная страница'}
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title="Главная страница")
				
		return dict(list(context.items()) + list(c_def.items()))

	def get_queryset(self):
		return Sbor.objects.filter(is_published=True)


# def index(request):
# 	posts = Sbor.objects.all()
	
# 	return render(request, 'sbor/index.html', {'posts':posts, 'menu': menu, 'title': 'Main page', 'cat_selected': 0 },)

def about(request):
	return render(request, 'sbor/about.html', {'menu': menu, 'title': 'About page'})

def test(request,test):
	return HttpResponse(f"Main page is of my site {test}")	

def addpage(request):
  
	return HttpResponse("Способы оплаты")
 
def contact(request):
  
	return HttpResponse("Обратная связь")
 
def login(request):

	return HttpResponse("Контакты")


class ShowPost(DataMixin, DetailView):
	model = Sbor
	template_name = 'sbor/post.html'
	slug_url_kwarg = 'post_slug'	
	context_object_name = 'post'
	def get_context_data(self, *, object_list=None, **kwargs): 
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title=context['post'])
		return dict(list(context.items()) + list(c_def.items()))	

#def show_post(request, post_slug):
	# post = get_object_or_404(Sbor, slug=post_slug)
 
	# context = {
	# 	'post': post,
	# 	'menu': menu,
	# 	'title': post.title,
	# 	'cat_selected': post.cat_id,
	# }
 
	# return render(request, 'sbor/post.html', context=context)	




class SborCategory(DataMixin, ListView):
	model = Sbor
	template_name = 'sbor/index.html'
	context_object_name = 'posts'
	allow_empty = False
	#cat1 = get_object_or_404(Category, slug =cat_slug)

	def get_queryset(self):
		return Sbor.objects.filter(cat_id__slug=self.kwargs['cat_slug'], is_published=True)

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat_id), cat_selected=context['posts'][0].cat_id)
 
		return dict(list(context.items()) + list(c_def.items()))

	# def get_context_data(self, *, object_list=None, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['title'] = 'Категория - ' + str(context['posts'][0].cat_id)
	# 	context['menu'] = menu
	# 	context['cat_selected'] = context['posts'][0].cat_id
	# 	return context



# def show_cat(request, cat_slug):
   
#     cat = Category.objects.all()
#     cat1 = get_object_or_404(Category, slug =cat_slug)
#     posts = Sbor.objects.filter(cat_id=cat1.id)

#     if len(posts) == 0:
#         raise Http404()

#     context = {
#         'posts': posts,
#         'cat': cat,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat1.id,
#     }

#     return render(request, 'sbor/index.html', context=context)


def pageNotFound(request, exception):
	return HttpResponseNotFound('<h1>Страница не найдена</h1>')
