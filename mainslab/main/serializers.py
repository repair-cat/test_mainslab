from rest_framework import serializers

from .models import *


class SnippetSerializer(serializers.ModelSerializer):
    """
    Строка запроса
    """
    str = serializers.SlugRelatedField(slug_field='str', queryset=StringRequest.objects.all())

    class Meta:
        model = Snippet
        fields = '__all__'


class StringRequestSerializer(serializers.ModelSerializer):
    """
    Строка запроса
    """
    # snippets = SnippetSerializer(many=True)

    class Meta:
        model = StringRequest
        fields = '__all__'