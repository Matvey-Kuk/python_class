from rest_framework import viewsets

from .models import Mark
from .serializers import MarkSerializer


class MarkViewSet(viewsets.ModelViewSet):
    serializer_class = MarkSerializer
    queryset = Mark.objects.all()
