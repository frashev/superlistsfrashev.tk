from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Instead of building our own HttpsResponse, we now use the Django render
# function. It takes the request as its first parameter and the name of the
# template to render.
def home_page(request):
    return render(request, 'home.html')
