from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.forms import ItemForm
from lists.models import Item, List
from django.core.exceptions import ValidationError

# Create your views here.
# Instead of building our own HttpsResponse, we now use the Django render
# function. It takes the request as its first parameter and the name of the
# template to render.
def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            form.save(for_list=list_)
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, "form": form})

# new_list creates a new item
def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        # Item.objects.create(text=request.POST['text'], list=list_)
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})
