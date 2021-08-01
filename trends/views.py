from django.shortcuts import render

# Create your views here.
from trends.stats.twitter.trends import get_trends
from trends.tasks.trends import get_eksisozluk_trends_job


def home(request):
    twitter_trends = get_trends()
    context = {'twitter_trends': twitter_trends}
    get_eksisozluk_trends_job()
    return render(request, 'trends/list.html', context)
