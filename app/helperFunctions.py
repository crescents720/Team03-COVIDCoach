from newsapi import NewsApiClient
import pandas as pd
import requests
import json


def get_news_list():
    newsapi = NewsApiClient(api_key="31119c92ed55433d9083373aba50327b")
    topheadlines = newsapi.get_top_headlines(q='covid' or 'coronavirus', language='en', page_size=100)

    articles = topheadlines['articles']

    news_description = []
    news_title = []
    news_image = []
    news_url = []

    for i in range(len(articles)):
        myarticles = articles[i]
        news_title.append(myarticles['title'])
        news_description.append(myarticles['description'])
        news_image.append(myarticles['urlToImage'])
        news_url.append(myarticles['url'])

    news_list = zip(news_title, news_description, news_image, news_url)

    # dataframe = pd.DataFrame(articles)
    return news_list


def get_stats_list():
    headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "4d79bf1779msh12322835c66a566p1dc930jsnaa9f4295d835"
    }

    # Get latest data for whole world.
    url_Totals = "https://covid-19-data.p.rapidapi.com/totals"
    querystring_Totals = {"format": "json"}
    response_Totals = requests.request("GET", url_Totals, headers=headers, params=querystring_Totals)
    obj = response_Totals.json()
    data_world = obj[0]

    # Get latest data for specific country. (in this case, USA)
    url_USA = "https://covid-19-data.p.rapidapi.com/country"
    querystring_USA = {"format": "json", "name": "USA"}
    response_USA = requests.request("GET", url_USA, headers=headers, params=querystring_USA)
    obj = response_USA.json()
    data_USA = obj[0]
    data_USA_1 = {'confirmed': data_USA['confirmed'], 'recovered': data_USA['recovered'],
                  'critical': data_USA['critical'], 'deaths': data_USA['deaths']}

    list_of_two_dicts = [data_world, data_USA_1]
    print(list_of_two_dicts[0])
    print(list_of_two_dicts[1])

    return list_of_two_dicts


