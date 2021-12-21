from rest_framework import viewsets
from .serializers import StringRequestSerializer, SnippetSerializer
from .models import StringRequest, Snippet
from .logic import get_data


class SnippetView(viewsets.ModelViewSet):
    """
    Просмотр сниппетов по запросу.
    """

    def get_serializer_class(self):
        """выбор сериализатора в зависимости от применяемого метода"""
        if self.action == 'list':
            return SnippetSerializer
        return StringRequestSerializer

    def get_queryset(self):
        """
        Вывести сниппеты конкретного запроса
        """
        str_request = StringRequest.objects.get(str=self.request.data['str'])
        return Snippet.objects.filter(str=str_request)

    def perform_create(self, serializer):
        """
        сохранение сключевого слова запроса и сниппетов по данному запросу
        """
        word = self.request.data['str']
        data = get_data(self.request.data['str'])    # словарь данных с сайта

        word_obj = StringRequest.objects.create(str=word)
        word_obj.save()

        for value in data.values():
            if len(value) > 0:

                snippet = Snippet.objects.create(
                    str=word_obj,
                    title=value['title'],
                    description=value['description'],
                    url=value['url']
                )
                snippet.save()

