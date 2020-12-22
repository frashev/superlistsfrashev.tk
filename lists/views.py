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
    error = None

    if request.method == 'POST':
        # Make some validation
        try:
            item = Item(text=request.POST['text'], list=list_)
            item.full_clean()
            item.save()
            # redirect(list_) gets the url of the object's ID passed
            return redirect(list_)
        except ValidationError:
            error = "You can't have an empty list item"

    return render(request, 'list.html', {'list': list_, 'error': error})

# new_list creates a new item
def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    # takes the object we want to redirect to, and it uses get_absolute_url
    # in object definitions in models.py
    return redirect(list_)
