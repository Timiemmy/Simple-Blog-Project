from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Importing for search
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from .forms import SearchForm
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


class Post_search(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Post.objects.annotate(search=SearchVector('title', 'content')).filter(search=query)
