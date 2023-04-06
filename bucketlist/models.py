from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class List(models.Model):
    user_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_name"
    )
    title = models.CharField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(null=False, blank=False, default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bucketlist')
