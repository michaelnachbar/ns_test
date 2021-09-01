from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import Http404

from datetime import datetime


from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView



from products.models import Category,Product



# Create your views here.

class CreateCategoryView(CreateView):
    model = Category
    template_name = 'create_category.html'
    fields = '__all__'
    success_url = "create_category"

class CategoryListView(ListView):

    model = Category
    paginate_by = 100 
    template_name = 'categories.html'


    def get_context_data(self, **kwargs):
        context = super(CategoryListView,self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context

class ProductListView(ListView):

    model = Product  # if pagination is desired
    template_name = 'products.html'


    def get_context_data(self, **kwargs):
        context = super(ProductListView,self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context


class CreateProductView(CreateView):
    model = Product
    #template_name = 'create_product.html'
    fields = '__all__'
    success_url = "/products"

class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'product_update_form.html'
    success_url = '/products'
    

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = '/products'


class ProductViewbyCategory(ListView):
    template_name = 'products.html'
    def get_queryset(self): 
        try:        
            print(self.args[0])
            print(type(self.args[0]))
            print(Category.objects.get(category_code = int(self.args[0])))
            self.category = Category.objects.get(category_code = self.args[0])
            print(self.category)
            return Product.objects.filter(category=self.category)
        except:
            f = open('error_log.txt','a')
            f.write(str(datetime.now()) + ': category code ' + str(self.args[0]) + ' not valid.')
            f.write('\n')
            raise Http404("Not a valid category code")



