from flask import render_template, flash, redirect, url_for

from app import app, bcrypt, db
from app.forms import RegisterForm
from app.models import User

from app.helperFunctions import get_news_list
from app.helperFunctions import get_stats_list
import sqlite3

@app.route('/')
def index():
    title = 'COVID Coach'
    listOf2 = get_stats_list()
    world_dict = listOf2[0]
    usa_dict = listOf2[1]
    return render_template('index.html', world=world_dict, usa=usa_dict, title=title)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Registration Success', category='success')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/news')
def news_page():
    title = 'COVID Coach Get News'
    news_list = get_news_list()
    return render_template('news.html', context=news_list, title=title)

@app.route('/news_detail/<key>')
def news_detail_page(key):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM news_table where news_id = ?',(key))
    fetched_item = c.fetchone()
    print(fetched_item[0])
    print(fetched_item[1])
    print(fetched_item[2])
    pass_context = (fetched_item[0],fetched_item[1],fetched_item[2],fetched_item[3],fetched_item[4],fetched_item[5],fetched_item[6],fetched_item[7])
    return render_template('news_detail.html', context = pass_context)


@app.route('/help')
def instruction_page():
    title = 'COVID Coach Get Help'
    return render_template('help.html', title=title)

@app.route('/board')
def board_page():
    title = 'COVID Coach Message Board'
    return render_template('board.html', title=title)