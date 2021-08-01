import requests
from bs4 import BeautifulSoup


def get_eksisozluk_trends():
    req = requests.get("https://eksisozluk.com/", headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0', })

    soup = BeautifulSoup(req.text, "html")
    eksisozluk_trend_list = []

    for ul_tag in soup.find_all('ul', {'class': 'topic-list'}):
        for li_tag in ul_tag.find_all('li'):
            for li_tag_ in ul_tag.find_all('li')[:14]:
                for a_href in li_tag_.find_all('a'):
                    eksisozluk_trend_dict = {}
                    number_of_entry = a_href.find_all('small')[0].text
                    entry = a_href.text.replace(" " + number_of_entry, "")
                    trend_link = "https://www.eksisozluk.com" + a_href['href']
                    # trend_desc = get_trend_details(trend_link)
                    entry_id = trend_link.replace("?a=popular", "")[-7:]
                    eksisozluk_trend_dict["entry"] = entry
                    eksisozluk_trend_dict["entry_id"] = entry_id
                    eksisozluk_trend_dict["#entry"] = number_of_entry
                    eksisozluk_trend_dict["trend_link"] = trend_link
                    # eksisozluk_trend_dict["trend_desc"] = trend_desc
                    eksisozluk_trend_list.append(eksisozluk_trend_dict)
            break

        return eksisozluk_trend_list


def get_trend_details(trend_link):
    req = requests.get("https://eksisozluk.com/", headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0', })

    soup = BeautifulSoup(req.text, "html")
    entry_desc_1 = soup.find_all('ul', {'id': 'entry-item-list'})[0]
    entry_desc_2 = entry_desc_1.find_all('li')
    trend_desc = str(entry_desc_2[0].find_all('div', {'class': 'content'})[0])

    return trend_desc
