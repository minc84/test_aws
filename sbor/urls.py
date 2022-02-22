from django.urls import path
 
from .views import *
 
urlpatterns = [
    path('', SborHome.as_view(), name='home'),
    path('test/<slug:test>/', test),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('cat/<slug:cat_slug>/', SborCategory.as_view(), name='cat'),
]
