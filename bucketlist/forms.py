from .models import List
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class AddBucketlistForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ('title', 'user_name')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Please enter your Bucketlist Item Here!'
                }),
            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'user',
                'type': 'hidden',
                }),
        }


class UpdatePlanningForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['planning', ]
        widgets = {
            'planning': forms.CharField(widget=SummernoteWidget())
        }
