from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='shop_home'),
    path('about/', views.about, name='about_us'),
    path('contact/', views.contact, name='contact_us'),
    path('tracker/', views.tracker, name='tracking_status'),
    path('search/', views.search, name='search'),
    path('product_view/<int:my_id>', views.product_view, name='product_view'),
    path('check_out/', views.check_out, name='check_out')
]