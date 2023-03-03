from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm
from django.utils import timezone


def post_list(request):
    posts = Post.published.all()
    # Adding pagination

    page_number = request.GET.get('page', 1)
    paginator = Paginator(posts, 2)
    # Pagination with 2 posts per page

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:  # If page_number is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:  # If page_number is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, "blog/list.html", {"posts": posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post,
                             publish__year=year, publish__month=month, publish__day=day)
    return render(request, "blog/detail.html", {"post": post})


def AddPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})


def EditPost(request):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/create_post.html', {'form': form})
