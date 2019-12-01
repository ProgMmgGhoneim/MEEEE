from django.shortcuts import render ,get_object_or_404 ,redirect
from django.views.generic.edit import FormMixin
from django.db.models import F
from django.forms import formset_factory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.urls import reverse
from django.views.generic.edit import UpdateView ,DeleteView
from django.urls import reverse_lazy

from django import forms
from django.views.generic import (
    ListView ,
    DetailView ,
    CreateView,
)
from .models import (
    category ,
    post ,
    comment ,
)
from .forms import (
    PostForm ,
    CategoryForm,
    CommentForm,
)

USER =settings.AUTH_USER_MODEL
# Create your views here.
def PostList(request):
    post_list = post.objects.all()
    post_count = post.objects.count()
    img_qr = post.objects.order_by('-num_viwes')[:3]
    categorylist = category.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 10)
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    template_name = 'main_content.html'

    context = {'post_list':post_list , 'slide_post' :img_qr,'post_count':post_count ,'categorylist':categorylist }
    return render (request , template_name , context)

class PostDetail(FormMixin,DetailView):
    queryset = post.objects.all()
    template_name = 'post_details.html'
    model = post
    form_class = CommentForm

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PostDetail , self).get_context_data(**kwargs)
        pk=self.kwargs['pk']
        view = post.objects.filter(pk=pk).update(num_viwes=F('num_viwes')+1)
        context['postlist'] = post.objects.all().order_by('-num_viwes')[:3]
        context['categorylist'] = category.objects.all()
        context['form'] = CommentForm(initial={'post': self.object , 'user':self.request.user})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PostDetail, self).form_valid(form)

def PostCreate(request):
    form = PostForm(request.POST or None ,request.FILES or None)
    if form.is_valid() :
        obj = form.save(commit =False)
        obj.user = request.user
        obj.save()
        form.save()
        form =PostForm()
        return redirect('post_list')
    template_name = 'crate_form.html'
    context ={'form':form }
    return render(request , template_name ,context)

def PostUpdate(request , pk):
    obj = post.objects.filter(pk=pk).first()
    form = PostForm(request.POST or None  ,request.FILES or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    template_name = 'update_form.html'
    context ={'form':form}
    return render(request , template_name ,context)

def PostDelete(request , pk):
    obj = get_object_or_404(post , pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('post_list')
    template_name = 'post_delete.html'
    context ={'obj':obj}
    return render(request , template_name ,context)

def base(request):
    category_list = category.objects.all()
    popular_post = post.objects.all()
    latest_post = post.objects.order_by('-timestamp')[:3]
    template_name = '../templates/base.html'
    context = {'category_list':category_list , 'popular_post' :popular_post ,'latest_post':latest_post}
    return render (request , template_name , context)

def ctegoryCreate(request):
    form = CategoryForm(request.POST or None ,request.FILES or None)
    if form.is_valid() :
        obj = form.save(commit =False)
        if not category.objects.filter(category= form.cleaned_data['category']).exists():
            obj.save()
            form.save()
            form =PostForm()
            return redirect('post_create')
        else:
            raise forms.ValidationError('Alreday token')
    template_name = 'categorycreate.html'
    context ={'form':form }
    return render(request , template_name ,context)

def CommentCreate(request , pk):
    form = CommmentForm(request.POST)
    print(request.user)
    if request.method == 'POST':
        if form.is_valid() :
            obj = form.save(commit =False)
            obj.user = request.user
            obj.post = request.GET.get('post_text')
            obj.save()
            form.save()
            return redirect('post_detail')
        else:
            form =CommmentForm()
    template_name = 'comment.html'
    context ={'form':form }
    return render(request , template_name ,context)

class CommentUpdate(UpdateView):
    model = comment
    queryset = comment.objects.all()
    fields =('txt' ,'user')
    template_name = 'comment_update.html'

class CommentDelete(DeleteView):
    model = comment
    template_name = 'comment_delete.html'
    success_url = reverse_lazy('post_detail')
