from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import current_user, login_required
from app import db
from app.models import User, Table, Task
from app.web.main import bp

@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    users = User.query.all()
    rows = list()
    for user in users:
        rows.append([user.username, str(user.last_seen), user.tables.count()]) #
    return render_template('index.html', title = 'Home', posts = [], cols = ('Имя пользователя', 'Дата последней активности', 'Количество таблиц'), rows = rows, table_title = 'Все пользователи')

@bp.route('/user/<username>')
@login_required
def user_show(username):
    user = User.query.filter_by(username = username).first_or_404()
    rows = list()
    return render_template('user.html', user = user, cols = ('Название', 'Статус', 'Название таблицы', 'Количество баллов', 'Дата начала выполнения', 'Дата завершения выполнения'), rows = rows, table_title = 'Задания')







