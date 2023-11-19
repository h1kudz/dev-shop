from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name= 'Название категории')
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Тег")
    description = models.TextField(blank = True,
                                   verbose_name='Описание категории')

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, verbose_name= 'Тег')
    image = models.FileField(upload_to='products/%Y/%m/%d', blank=True, verbose_name= 'Картинки')
    description = models.TextField(blank=True, verbose_name='Описание')
    new_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Новая цена")
    old_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Старая цена")
    is_available = models.BooleanField(default=True, verbose_name="В наличии")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата добаления")
    updated = models.DateTimeField(auto_now=True)
    #count = models.IntegerField(verbose_name="Количество")
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-pub_date']),
            ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name