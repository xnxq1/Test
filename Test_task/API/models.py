from django.db import models

# Create your models here


class Type(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип упражнения'
        verbose_name_plural = 'Тип упражнения'


class Exercises(models.Model):
    DIFFICULT_CHOICES = (
        ('Начинающий', 'Начинающий'),
        ('Средний', 'Средний'),
        ('Продвинутый', 'Продвинутый'))
    name = models.CharField(max_length=255, verbose_name='Название', unique=True)
    description = models.TextField(max_length=500, verbose_name='Описание')
    type = models.ForeignKey(to_field='id', to=Type, on_delete=models.PROTECT, verbose_name='Тип упражнения')
    difficult = models.CharField(choices=DIFFICULT_CHOICES, max_length=255, verbose_name='Уровень сложности')
    number_of_repetitions = models.PositiveIntegerField(default=0, verbose_name='Количество повторений')
    number_of_approaches = models.PositiveIntegerField(default=0, verbose_name='Количество подходов')
    time = models.PositiveIntegerField(default=0, verbose_name='Время выполнения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'

