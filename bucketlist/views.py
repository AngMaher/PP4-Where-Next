from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import generic, View
from .models import List
from django.urls import reverse_lazy
from django.contrib import messages
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

    def post(self, request, *args, **kwargs):
        queryset = List.objects.all()

        add_item_form = AddBucketlistForm(data=request.POST)

        if add_item_form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'Successfully added a comment.')
        else:
            Add_item_form = AddBucketlistForm()

        def get_object(self):
            return self.request.user



class UpdateListItem(generic.UpdateView):
    model = List
    template_name = 'userbucketlist/update_list_item.html'
    fields = ['title', 'done']


class DeleteListItem(generic.DeleteView):
    model = List
    template_name = 'userbucketlist/delete_list_item.html'
    success_url = reverse_lazy('bucketlist')


class StorePlanning(generic.ListView):
    model = List
    queryset = List.objects.all()
    template_name = 'userbucketlist/store_planning.html'
    fields = ['planning']


class UpdatePlan(generic.UpdateView):
    model = List
    template_name = 'userbucketlist/update_planning.html'
    fields = ['planning']
