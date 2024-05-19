from django.shortcuts import render
from . models import Item

def first_page(request):
    return render(request, 'index.html')

def page(request, pk):
    nav_objects = Item.objects.values('id','item_nav', 'item_nav_position').filter(item_nav_position__gt=0).order_by('-item_nav_position')
    print("nav_objects: ", nav_objects)
    content_object = Item.objects.values().get(item_nav_position=pk)
    print("content_object:\n", content_object)
    context = {'pk': pk, 'nav_objects': nav_objects, 'content_object': content_object}
    return render(request, 'page.html', context)
