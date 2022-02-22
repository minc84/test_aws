from django.db import models
from django.urls import reverse

# Create your models here.
class Sbor(models.Model):
	title = models.CharField(max_length=255, verbose_name = 'Заголовок')
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
	content = models.TextField(blank=True)
	photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
	time_create = models.DateTimeField(auto_now_add=True)
	time_update = models.DateTimeField(auto_now=True)
	is_published = models.BooleanField(default=True)
	cat_id = models.ForeignKey('Category', on_delete=models.PROTECT)

	def __str__(self):
		return self.title



	def get_absolute_url(self):
		return reverse('post', kwargs={'post_slug': self.slug})


	class Meta:
		verbose_name = 'Сборка мебели'
		verbose_name_plural = 'Сборка мебели'
		ordering = ['time_create', 'title']


class Category(models.Model):
	name = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
 
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('cat', kwargs={'cat_slug': self.slug})


	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'
		ordering = ['id']

	