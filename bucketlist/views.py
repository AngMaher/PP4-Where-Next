from django.shortcuts import render, HttpResponse
from django.views import generic
from .models import List


class UserList(generic.ListView):
    model = List
    template_name = 'bucketlist.html'
