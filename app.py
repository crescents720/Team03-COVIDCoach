from flask import Flask, render_template
from newsapi import NewsApiClient
import pandas as pd
import initDB as iDB

app = Flask(__name__)

@app.route('/')
def index():
    title = 'COVID Coach'
    return render_template('index.html', title=title)


@app.route('/news')
def news_page():
    title = 'COVID Coach Get News'

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

    newsl_list = zip(news_title, news_description, news_image, news_url)

    return render_template('news.html', context=newsl_list, title=title)

    dataframe = pd.DataFrame(articles)

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/initDB')
def init_db():
    title = 'COVID Coach'
    handler = iDB.initDB()
    handler.run()
    return render_template('index.html', title=title)

@app.route('/help')
def help_page():
    title = 'COVID Coach Get Help'
    return render_template('help.html', title=title)

@app.route('/board')
def board_page():
    title = 'COVID Coach Message Board'
    return render_template('board.html', title=title)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
