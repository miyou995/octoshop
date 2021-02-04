
from django.urls import path
from . import views
from .views import  IndexView
app_name = 'main'
urlpatterns = [

    # path('produits/', ProductsView.as_view(), name='products'),
    path('<slug:slug>/<int:id>', views.productDetail, name='product-detail'),
    path('produits/', views.product_list, name='products'),
    path('<slug:category_slug>/', views.product_list, name='prod-by-cat'),
    path('<slug:category_slug>/', views.product_list, name='prod-by-sub-cat'),
    path('', views.IndexView.as_view(), name='index'),

]
