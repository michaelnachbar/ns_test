"""ns_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from products.views import CreateCategoryView, CategoryListView, ProductListView, CreateProductView, ProductUpdateView, \
    ProductDeleteView, ProductViewbyCategory

urlpatterns = [
    url(r'^admin/', admin.site.urls),  
    url(r'^create_category', CreateCategoryView.as_view()), 
    url(r'^categories', CategoryListView.as_view()), 
    url(r'^products', ProductListView.as_view()),
    url(r'^createproduct', CreateProductView.as_view()),
    url(r'^updateproduct/(?P<pk>[-\w]+)/$', ProductUpdateView.as_view()),
    url(r'^deleteproduct/(?P<pk>[-\w]+)/$', ProductDeleteView.as_view()),
    url(r'^productcategory/([\w-]+)/$', ProductViewbyCategory.as_view()),
]
