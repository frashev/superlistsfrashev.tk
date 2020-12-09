from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.
# Instead of building our own HttpsResponse, we now use the Django render
# function. It takes the request as its first parameter and the name of the
# template to render.
def home_page(request):
    return render(request, 'home.html')

# view_list display items to the screen
def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

# new_list creates a new item
def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')
