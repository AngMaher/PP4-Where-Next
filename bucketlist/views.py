from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import generic, View
from .models import List
from django.urls import reverse_lazy


class UserList(generic.ListView):
    model = List
    queryset = List.objects.all()
    template_name = 'userbucketlist/bucketlist.html'


# class PostBucketlist(View):

#     def get(self, request, *args, **kwargs):
#         current_user = request.user
#         queryset = List.objects.filter(current_user)
#         list = get_object_or_404(queryset)

#         return render(
#             request,
#             "userbucketlist/bucketlist.html",
#             {
#                 "list": list,
#             },
#         )


class AddListItem(generic.CreateView):
    model = List
    template_name = 'userbucketlist/add_list_item.html'
    fields = '__all__'


class UpdateListItem(generic.UpdateView):
    model = List
    template_name = 'userbucketlist/update_list_item.html'
    fields = ['title','done']


class DeleteListItem(generic.DeleteView):
    model = List
    template_name = 'userbucketlist/delete_list_item.html'
    success_url = reverse_lazy('bucketlist')
