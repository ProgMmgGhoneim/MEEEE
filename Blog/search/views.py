from django.shortcuts import render
from django.db.models import Q

from .models import search_model
from posts.models import post


# Create your views here.
def search_view (request):
    q =request.GET.get('query' , None)
    user=None
    context ={'query':q}
    if request.user.is_authenticated:
        user = request.user
        search_model.objects.create(user=user ,query=q)
        lookup=(Q(title__icontains=q) |
                Q(content__icontains =q))
        blog_list = post.objects.filter(lookup)
        context['blog_list'] =blog_list

    return render(request ,'search.html' ,context)
