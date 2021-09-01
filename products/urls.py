from django.urls import path

from . import views

urlpatterns = [
    # ex: /add_category/
    
    path('create_category', views.CreateCategoryView, name='create_category'),
]
