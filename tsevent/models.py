from django.db import models
from django.utils import timezone
# Create your models here.



class tsevent(models.Model):
    ide = models.CharField(verbose_name='Nomber Event', db_index=True, max_length=10)
    note = models.CharField(verbose_name='note for Event', max_length=255)
    create_date = models.DateTimeField(default=timezone.now)
