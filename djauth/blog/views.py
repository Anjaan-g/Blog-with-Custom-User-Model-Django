from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .models import BlogPost
from blog.forms import BlogPostModelForm


def blog_post_list_view(request):
    #list out objects
    #All at a same time
    qs = BlogPost.objects.all().published()
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user = request.user)
        qs = (qs | my_qs).distinct()
    template_name = 'blog/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

# @login_required
@staff_member_required
def blog_post_create_view(request):
    #create objects
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit = False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
    template_name = 'blog/form.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    #retrieve objects
    #one at a time
    obj = get_object_or_404(BlogPost, slug = slug)
    template_name = 'blog/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


@staff_member_required
def blog_post_update_view(request,slug):
    obj = get_object_or_404(BlogPost, slug = slug)
    form = BlogPostModelForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
    template_name = 'blog/form.html'
    context = { "title": f"Update {obj.title}", "form": form}
    return render(request, template_name, context)


@staff_member_required
def blog_post_delete_view(request,slug):
    obj = get_object_or_404(BlogPost, slug = slug)
    template_name = 'blog/delete.html'
    if request.method == 'POST':
        obj.delete()
        return redirect("/blog")
    context = {"object": obj}
    return render(request, template_name, context)

# @staff_member_required
# def blog_post_comment_view(request,slug):
#     qs = Comment.objects.all()
#     template_name = 'blog/comment.html'
#     form = CommentForm(request.POST or None)
#     if form.is_valid():
#         obj = form.save(commit = False)
#         obj.save()
#         form = CommentForm()
#     context={'form':form, "blog_post":qs}
#     return render(request, template_name, context)
