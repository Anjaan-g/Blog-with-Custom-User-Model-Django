from django.conf import settings
from django.db import models
from users.models import CustomUser

class SearchQuery(models.Model):
    user =models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.SET_NULL)
    query =models.CharField(max_length=220)
    timestamp =models.DateTimeField(auto_now_add=True)
