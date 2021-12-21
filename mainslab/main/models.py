from django.db import models


class StringRequest(models.Model):
    str = models.CharField(max_length=20, verbose_name='Строка запроса')

    class Meta:
        verbose_name = 'Строка запроса'
        verbose_name_plural = 'Строки запроса'
        db_table = 'strings'

    def __str__(self):
        return self.str

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """
        При сохранении объекта проверяем существует ли объект с такой же строкой.
        Если да, то удаляем его и все связанные с ним сниппеты так же удаляются
        """
        if StringRequest.objects.filter(str=self.str).exists():
            StringRequest.objects.get(str=self.str).delete()
        super(StringRequest, self).save()


class Snippet(models.Model):
    str = models.ForeignKey(StringRequest, on_delete=models.CASCADE, verbose_name='Строка запроса',
                            related_name='snippets')
    title = models.CharField(max_length=300, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    url = models.URLField(verbose_name='Ссылка')

    class Meta:
        ordering = ('str',)
        verbose_name = 'Сниппет'
        verbose_name_plural = 'Сниппеты'
        db_table = 'snippets'

    def __str__(self):
        return self.title