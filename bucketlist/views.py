from django.shortcuts import render, HttpResponse
from django.views import generic, View
from .models import List


class UserList(generic.ListView):
    model = List
    template_name = 'userbucketlist/bucketlist.html'


# class PostBucketlist(View):

#     def get(self, request, slug, *args, **kwargs):
#         queryset = Post.objects.all()
#         list = get_object_or_404(queryset)

#         return render(
#             request,
#             "bucketlist.html",
#             {
#                 "list": list,
#             },
#         )