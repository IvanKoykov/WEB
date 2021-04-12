from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from django.views.generic import View
from .models import Post, Tag
from .utils import *
from django.urls import reverse


def home_page(request):
    return render(request, 'home.html')


def home_news(request):
    posts = Post.objects.all()
    return render(request, 'index.html', context={'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags_list.html', context={'tags':tags})


class TagDetail(ObjectDetailMixin,View):
    model=Tag
    tenplate = 'tag_detail.html'


class TagCreate(ObjectCreateMixin,View):
    model_form=TagForm
    template = 'tag_create.html'
    # def get(self,request):
    #     form=TagForm
    #     return render(request,'tag_create.html', context={'form':form})
    #
    # def post(self,request):
    #    bound_form=TagForm(request.POST)
    #
    #    if bound_form.is_valid():
    #        new_tag = bound_form.save()
    #        return redirect(new_tag)
    #    return render(request,'tag_create.html',context={'form':bound_form})


class TagUpdate(ObjectUpdateMixin,View):
    model = Tag
    model_form = TagForm
    templete = 'tag_update.html'
    # def get(self, request, slug):
    #     tag=Tag.objects.get(slug__iexact=slug)
    #     bound_form=TagForm(instance=tag)
    #     return render(request,'tag_update.html', context={'form': bound_form, 'tag': tag})
    #
    # def post(self,request,slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(request.POST, instance=tag)
    #
    #     if bound_form.is_valid():
    #         new_tag=bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'tag_update.html', context={'form':bound_form, 'tag':tag})


class TagDelete(ObjectDeleteMixin,View):
    model=Tag
    template = 'tag_delete.html'
    redirect_url = 'tags_list_url'


class PostCreate(ObjectCreateMixin,View):
    model_form=PostForm
    template = 'post_create.html'


class PostDelete(ObjectDeleteMixin,View):
    model=Post
    template = 'post_delete.html'
    redirect_url = 'home_news_url'


class PostDetail(ObjectDetailMixin,View):
    model = Post
    tenplate = 'post_detail.html'


class PostUpdate(ObjectUpdateMixin,View):
    model = Post
    model_form = PostForm
    templete = 'post_update.html'


