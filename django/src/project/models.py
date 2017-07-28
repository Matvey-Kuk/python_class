import uuid

from django.db import models


class Mark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mark = models.CharField(max_length=20, default="color:red")
