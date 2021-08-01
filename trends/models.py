from django.db import models

# Create your models here.


class EksiSozlukTrend(models.Model):
    trend_id = models.TextField()
    trend_name = models.TextField()
    time_range = models.IntegerField()
    trend_order = models.IntegerField()
    trend_date_time = models.DateTimeField()


class EksiSozlukTrendDetails(models.Model):
    trend_id = models.TextField()
    trend_link = models.TextField()
    trend_desc = models.TextField()