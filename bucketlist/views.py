from django.shortcuts import render
from django.views import generic
from .models import List


class List(generic.ListView):
    model = List
    queryset = List.objects.filter().order_by('-created_on')
    template_name = 'bucketlist.html'
