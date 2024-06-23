from django.db import models
from utils.models import CoreModel   


class TestDemo(CoreModel):
        
    des = models.TextField(null=True, blank=True, verbose_name='Описание', help_text='Описание')    
    code = models.DecimalField(null=True, blank=True, max_digits = 13, decimal_places = 4, verbose_name='Код', help_text='Код')    
    name = models.CharField(null=True, blank=True, max_length=255, verbose_name='Название', help_text='Название')

    class Meta:
        db_table = 'generator_test_demo'
        verbose_name = 'Тестовый пример'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)
    