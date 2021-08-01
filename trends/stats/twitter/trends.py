import requests

from trends.stats.twitter.api_connection import get_token


def get_trends():
    trend_list = []
    base_url = 'https://api.twitter.com/'
    access_token = get_token()
    req_headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }

    trend_params = {
        'id': 2344116,
    }

    trend_url = '{}1.1/trends/place.json'.format(base_url)
    trend_resp = requests.get(trend_url, headers=req_headers, params=trend_params)
    for trend in trend_resp.json()[0]["trends"]:
        trend_list.append(trend["name"])

    return trend_list
