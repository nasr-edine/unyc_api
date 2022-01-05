from django.views.generic import ListView
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Reference
from .serializers import ReferenceSerializer


class ReferenceListView(ListView):
    model = Reference
    template_name = "reference_list.html"


class ListReference(ListAPIView):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer


class DetailReference(RetrieveAPIView):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
