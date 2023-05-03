from django.shortcuts import render, HttpResponse, get_object_or_404, reverse, redirect  # noqa
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from django.contrib import messages
from .forms import CommentForm


class BlogPosts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


# Post class for the each blog post
class PostContent(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_content.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Successfully added a comment.')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_content.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.success(request, 'You have unliked the post')
        else:
            post.likes.add(request.user)
            messages.success(request, 'You have liked the post')

        return HttpResponseRedirect(reverse('post_content', args=[slug]))


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {
        'cats': cats,
        'category_posts': category_posts,
        })


def AboutView(request):
    return render(request, 'about.html')


# 404 Handler
def phandler_404(request, exception):
    return render(request, '404.html', status=404)


# 500 Handler
def handler_500(request, exception):
    response = render(request, '500.html')
    response.status_code = 500
    return response


# 403 Handler
def handler_403(request, *args, **argv):
    response = render_to_response('403.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 403
    return response
