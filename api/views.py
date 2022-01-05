from rest_framework.generics import ListAPIView

from references.models import Reference
from .serializers import ReferenceSerializer


class ReferenceAPIView(ListAPIView):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
