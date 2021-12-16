from django.urls import path
from app_shop.views import *

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:id>', product_detail, name='product_detail'),

    path('search-product', search_product, name='search_product'),

]