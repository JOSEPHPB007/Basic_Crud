from django.shortcuts import render,redirect,get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.


def create_item(request):
    if request.method=='POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_item')
    else:
        form=ItemForm()
    return render(request,'item_form.html',{'form':form})

def list_item(request):
    items= Item.objects.all()
    return render(request,'item_list.html',{'items':items})

def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    print('item:',item)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('list_item')        
    else:
        form=ItemForm(instance=item)
    return render(request,'item_form.html',{'form':form})

def delete_item(request,pk):
    item=get_object_or_404(Item,pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('list_item')
    return render(request,'item_confirm_delete.html',{'item':item})