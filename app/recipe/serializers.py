from rest_framework import serializers

from core.models import Tag


class TagsSerializer(serializers.ModelSerializer):
    """Serializer for tags objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)
