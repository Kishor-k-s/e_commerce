from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='blog_home'),
    path('blogpost/<int:id>', views.blogpost, name='blogpost'),
]
