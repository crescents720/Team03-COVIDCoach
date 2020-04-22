from flask import render_template, flash, redirect, url_for

from app import app, bcrypt, db
from app.forms import RegisterForm
from app.models import User

from app.helperFunctions import get_news_list
from app.helperFunctions import get_stats_list


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

@app.route('/help')
def instruction_page():
    title = 'COVID Coach Get Help'
    return render_template('help.html', title=title)

@app.route('/board')
def board_page():
    title = 'COVID Coach Message Board'
    return render_template('board.html', title=title)