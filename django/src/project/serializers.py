from rest_framework import serializers

from .models import Mark


class MarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mark
        fields = (
            'id',
            'mark'
        )
