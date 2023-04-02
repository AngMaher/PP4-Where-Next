from django.shortcuts import render, HttpResponse, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Bucketlist


class Bucketlist_Post(generic.ListView):
    model = Bucketlist
    queryset = Bucketlist.objects.filter(status=1).order_by('-created_on')
    template_name = 'bucketlist.html'


class PostList(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "bucketlist.html",
            {
                "post": post,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "bucketlist.html",
            {
                "post": post,
            },
        )