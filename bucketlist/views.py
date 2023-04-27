from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
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
    success_message = "You have successfully added a new item in your Bucket List!"  # noqa

    def form_valid(self, AddBucketlistForm):
        response = super().form_valid(AddBucketlistForm)
        success_message = self.get_success_message(
            AddBucketlistForm.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data


class UpdateListItem(generic.UpdateView):
    model = List
    template_name = 'userbucketlist/update_list_item.html'
    fields = ['title', 'done']
    success_message = "Update has completed successfully!"

    def form_valid(self, AddBucketlistForm):
        response = super().form_valid(AddBucketlistForm)
        success_message = self.get_success_message(
            AddBucketlistForm.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data


class StorePlanning(generic.DetailView):
    model = List
    queryset = List.objects.all()
    template_name = 'userbucketlist/store_planning.html'
    fields = ['planning']


class UpdatePlan(generic.UpdateView):
    model = List
    template_name = 'userbucketlist/update_planning.html'
    fields = ['planning']
    success_message = "Your plan has been updated! You are on your way to complete your dream!"  # noqa

    def form_valid(self, UpdatePlanningForm):
        response = super().form_valid(UpdatePlanningForm)
        success_message = self.get_success_message(
            UpdatePlanningForm.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data


def DeleteListItem(request, item_id):
    list_item = get_object_or_404(List, id=item_id)
    list_item.delete()
    messages.warning(request, "Recipe deleted!")
    return redirect('bucketlist')
