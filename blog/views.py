from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic import View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm


@login_required
def posts_list(request):
    posts=Post.objects.all()
    return render(request,'blog/index.html',context={'posts':posts})

@login_required
def tags_list(request):
    tags=Tag.objects.all()
    return render(request,'blog/tags_list.html',context={'tags':tags})


class PostDetail(LoginRequiredMixin,ObjectDetailMixin,View):
    model=Post
    template='blog/post_detail.html'

class TagDetail(LoginRequiredMixin,ObjectDetailMixin,View):
    model=Tag
    template='blog/tag_detail.html'
class TagCreate(LoginRequiredMixin,ObjectCreateMixin, View):
    model_form=TagForm
    template='blog/tag_create.html'
    raise_exception=True

    # def get(self,request):
    #     form=TagForm()
    #     return render(request,'blog/tag_create.html',context={'form':form})
    #
    # def post(self,request):
    #     bound_form=TagForm(request.POST)
        # if bound_form.is_valid():
        #     new_tag=bound_form.save()
        #     return redirect(new_tag)
        # return render(request,'blog/tag_create.html',context={'form':bound_form})

class TagUpdate(LoginRequiredMixin,ObjectUpdateMixin,View):
    model=Tag
    model_form=TagForm
    template='blog/tags_update_form.html'
    raise_exception=True
    # def get(self,request,slug):
    #     tag=Tag.objects.get(slug__iexact=slug)
    #     bound_form=TagForm(instance=tag)
    #     return render(request,'blog/tags_update_form.html',context={'form':bound_form,'tag':tag})
    #
    # def post(self,request,slug):
    #     tag=Tag.objects.get(slug__iexact=slug)
    #     bound_form=TagForm(request.POST, instance=tag)
    #     if bound_form.is_valid():
    #         new_tag=bound_form.save()
    #         return redirect(new_tag)
    #     return render(request,'blog/tags_update_form.html',context={'form':bound_form,'tag':tag})


class PostCreate(LoginRequiredMixin,ObjectCreateMixin,View):
    model_form=PostForm
    template='blog/post_create_form.html'
    raise_exception=True


    # def get(self,request):
    #     form=PostForm()
    #     return render(request,'blog/post_create_form.html',context={'form':form})
    #
    # def post(self,request):
    #     bound_form=PostForm(request.POST)
    #     if bound_form.is_valid():
    #         new_tag=bound_form.save()
    #         return redirect(new_tag)
    #     return render(request,'blog/post_create_form.html',context={'form':bound_form})

class PostUpdate(LoginRequiredMixin,ObjectUpdateMixin,View):
    model=Post
    model_form=PostForm
    template='blog/post_update_form.html'
    raise_exception=True

class TagDelete(LoginRequiredMixin,ObjetDeleteMixin,View):
    model=Tag
    template='blog/tag_delete_form.html'
    redirect_url='tags_list_url'
    raise_exception=True
    # def get(self,request,slug):
    #     tag=Tag.objects.get(slug__iexact=slug)
    #     return render(request,'blog/tag_delete_form.html',context={'tag':tag})
    #
    # def post(self,request,slug):
    #     tag=Tag.objects.get(slug__iexact=slug)
    #     tag.delete()
    #     return redirect(reverse('tags_list_url'))
class PostDelete(LoginRequiredMixin,ObjetDeleteMixin,View):
    model=Post
    template='blog/post_delete_form.html'
    redirect_url='posts_list_url'
    raise_exception=True

    # return HttpResponse('<h1>HOP!! HOP!!</h1>')
