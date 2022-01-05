from django.shortcuts import render
from django.views.generic import ListView
from .models import Reference
# Create your views here.


class ReferenceListView(ListView):
    model = Reference
    template_name = "reference_list.html"
