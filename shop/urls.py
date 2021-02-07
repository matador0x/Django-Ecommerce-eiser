from django.urls import path
from  . import views

app_name = 'shopy'
urlpatterns = [
    path('', views.product_list, name='shop'),
    path('<slug:category_slug>/', views.product_list, name='shop'),
    path('product_detail/<int:id>/<slug:slug>/', views.product_details, name='product_details'),

]
