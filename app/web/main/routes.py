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
        rows.append([(url_for('main.user_show', username = user.username), user.username), (user.last_seen,), user.tables.count()]) #
    return render_template('index.html', title = 'Home', posts = [], cols = ('Имя пользователя', 'Дата последней активности', 'Количество таблиц'), rows = rows, table_title = 'Все пользователи')
score_text = ('Не выполнено', 'Выполняется', 'Выполнено')
@bp.route('/user/<username>')
@login_required
def user_show(username):
    user = User.query.filter_by(username = username).first_or_404()
    tasks = user.tasks.all()
    rows = list()
    for task in tasks:
        start_time = (task.start_time,)
        finish_time = (task.finish_time,)
        time_itog = 0
        if start_time[0] is None or task.status == 0: start_time = 0
        if finish_time[0] is None or task.status != 2: 
            finish_time = 0
        else:
            time_itog = round((task.finish_time - task.start_time).total_seconds() / 60, 2)

        rows.append([score_text[task.status], task.score, start_time, finish_time, time_itog]) #
    return render_template('user.html', user = user, cols = ('Статус', 'Успешность выполнения', 'Дата начала выполнения', 'Дата завершения выполнения', 'Времени затрачено (минут)'), rows = rows, table_title = 'Задания')







