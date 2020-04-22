from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from helperFunctions import get_news_list
from helperFunctions import get_stats_list

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    title = 'COVID Coach'
    listOf2 = get_stats_list() 
    world_dict = listOf2[0]
    usa_dict = listOf2[1]
    return render_template('index.html', world=world_dict, usa=usa_dict, title=title)


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/news')
def news_page():
    title = 'COVID Coach Get News'
    news_list = get_news_list()
    return render_template('news.html', context=news_list, title=title)

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