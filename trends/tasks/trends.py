import datetime

from trends.models import EksiSozlukTrend
from trends.stats.eksisozluk.trends import get_eksisozluk_trends


def get_eksisozluk_trends_job():
    # close connection before acsess to the database to avoid mysql 206 error
    trend_list = get_eksisozluk_trends()
    now = datetime.datetime.now()

    trend_order = 10

    try:
        time_range = EksiSozlukTrend.objects.filter(trend_date_time__date=now).order_by('id').reverse()[0] \
                         .time_range + 1
    except:
        time_range = 1

    for trend in trend_list:
        eksi_sozluk_trend = EksiSozlukTrend(trend_name=trend["entry"], time_range=time_range,
                                            trend_order=trend_order, trend_date_time=now)
        eksi_sozluk_trend.save()

        trend_order -= 1

    print(time_range)
