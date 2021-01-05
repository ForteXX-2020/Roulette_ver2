from django.db import models
from django.utils import timezone

class Day(models.Model):
    date = models.DateTimeField('日付',default=timezone.now)
    number = models.IntegerField('出目',default=0)
    types = models.IntegerField('ルーレットタイプ',default=1)
    place = models.TextField('場所',default=0, max_length=10)
    company = models.TextField('製作会社',default=0, max_length=10)
    
