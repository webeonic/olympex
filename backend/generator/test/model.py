from django.db import models
from utils.models import CoreModel   


class Test(CoreModel):
        
    icon = models.CharField(null=True, blank=True, max_length=255, verbose_name='Иконка', help_text='Иконка')    
    sequence = models.DecimalField(null=True, blank=True, max_digits = 13, decimal_places = 4, verbose_name='Порядок сортировки', help_text='Порядок сортировки')    
    code = models.CharField(null=True, blank=True, max_length=255, verbose_name='Код', help_text='Код')    
    name = models.CharField(null=True, blank=True, max_length=255, verbose_name='Название', help_text='Название')

    class Meta:
        db_table = 'generator_test'
        verbose_name = 'Тестирование шаблона'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)
    