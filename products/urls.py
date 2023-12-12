from django.urls import path
from .views import index, show

app_name = 'product'

urlpatterns = [
    path('', index, name='home'),
    path('<slug:category_slug>/', index, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', show, name='product_show'),
]