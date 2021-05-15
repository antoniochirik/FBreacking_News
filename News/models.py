from django.db import models


class News(models.Model):
    head = models.CharField(
        max_length=250,
        verbose_name='Заголовок',
        unique=True
    )
    text = models.TextField(
        verbose_name='Текст новости'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.head
