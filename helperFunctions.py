from newsapi import NewsApiClient
import pandas as pd

def get_news_list():
	newsapi = NewsApiClient(api_key="31119c92ed55433d9083373aba50327b")
	topheadlines = newsapi.get_top_headlines(q='covid' or 'coronavirus',language='en',page_size=100)

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

	#dataframe = pd.DataFrame(articles)
	return news_list
	

	