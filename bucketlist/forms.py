from .models import List
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


# Form to Add a new bucket List item
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


# Form to Update Planning
class UpdatePlanningForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['planning', ]
        widgets = {
            'planning': forms.CharField(widget=SummernoteWidget())
        }
