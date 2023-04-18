from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import generic, View
from .models import List
from django.urls import reverse_lazy
from .forms import AddBucketlistForm


class UserList(generic.ListView):
    model = List
    queryset = List.objects.all()
    template_name = 'userbucketlist/bucketlist.html'


class AddListItem(generic.CreateView):
    model = List
    form_class = AddBucketlistForm
    template_name = 'userbucketlist/add_list_item.html'
    # fields = ['title', 'user_name', 'done']


class UpdateListItem(generic.UpdateView):
    model = List
    template_name = 'userbucketlist/update_list_item.html'
    fields = ['title', 'done']


class DeleteListItem(generic.DeleteView):
    model = List
    template_name = 'userbucketlist/delete_list_item.html'
    success_url = reverse_lazy('bucketlist')