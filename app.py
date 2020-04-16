from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    title = 'COVID Website'
    return render_template('index.html', title=title)

@app.route('/news')
def news_page():
    title = 'COVID Website Get News'
    return render_template('news.html', title=title)

@app.route('/help')
def help_page():
    title = 'COVID Website Get Help'
    return render_template('help.html', title=title)

@app.route('/board')
def board_page():
    title = 'COVID Website Message Board'
    return render_template('board.html', title=title)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)