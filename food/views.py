from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
#### This is function based views
# def index(request):
#     item_list=item.objects.all()
#     #template=loader.get_template('food/index.html')
#     context={
#         'item_list':item_list,
#     }
#     return render(request,'food/index.html',context)

class IndexClassView(ListView):
    model = item;
    template_name = 'food/index.html'
    context_object_name = 'item_list'


def items(request):
    return HttpResponse('this view is for item')

###This is function based view
# def detail(request,item_id):
#     Item=item.objects.get(pk=item_id)
#     context={
#         'item': Item,
#     return render(request,'food/detail.html',context)

class FoodDetail(DetailView):
    model = item
    template_name = 'food/detail.html'
#this is function based views
# def create_item(request):
#     form = ItemForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
#
#     return render(request,'food/item-form.html',{'form': form})

#This is class based views for create item
class CreateItem(CreateView):
    model=item;
    fields=['item_name','item_desc','item_price','item_image']
    template_name='food/item-form.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)


def update_item(request, id):
    items=item.objects.get(id=id)
    form=ItemForm(request.POST or None, instance=items)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item-form.html',{'form':form,'items':items})
def delete_item(request, id):
    items=item.objects.get(id=id)

    if request.method == 'POST':
        items.delete()
        return redirect('food:index')

    return render(request,'food/item-delete.html',{'items':items})