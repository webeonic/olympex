from django.db import models
from utils.models import CoreModel   


class TemplateTest(CoreModel):
        
    input_text_area_2 = models.TextField(null=True, blank=True, verbose_name='Текстовое поле', help_text='Текстовое поле')    
    input_1 = models.CharField(null=True, blank=True, max_length=255, verbose_name='Поле ввода', help_text='Поле ввода')

    class Meta:
        db_table = 'generator_template_test'
        verbose_name = 'Тест 1'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)
    