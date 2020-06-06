from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import current_user, login_required
from app import db
from app.models import User, Task, Table
from app.web.task import bp
from app.no_web.base_task import ManagerTask
from app.web.console import check_from


score_text = ('Не выполнено', 'Выполняется', 'Выполнено')
@bp.route('/all')
@login_required
def all_task(): 
    global score_text
    user = User.query.filter_by(username = current_user.username).first_or_404()
    rows = list()
    mode_close = False
    for e in ManagerTask.base_task.items():
        row = list()
        task = user.tasks.filter_by(task_id = e[0]).first()
        if task is None: 
            task = Task(task_id = e[0], status = 0, score = 0)
            user.tasks.append(task)
            db.session.add(task)
            db.session.commit()
        if mode_close:
            row.append(e[1].name)
        else:
            row.append((url_for('task.task', task_id = task.task_id), e[1].name))
        if task.status != 2: mode_close = True
        row.append(score_text[task.status])
        row.append(task.score)
        rows.append(row)
    return render_template('task/all_task.html', cols = ('Название', 'Статус выполнения', 'Успешность выполнения'), rows = rows, table_title = 'Все задания')

@bp.route('/<task_id>', methods=['GET', 'POST'])
@login_required
def task(task_id): 
    task = Task.query.filter_by(task_id = task_id).first_or_404()
    task_finish = Task.query.filter_by(status = 0).first()
    if not task_finish is None and task.id > task_finish.id: return redirect(url_for('task.task', task_id = task_finish.id))
    base_task = ManagerTask.get_task(task_id)
    name = base_task.name
    description = base_task.description
    instruction = base_task.instruction
    example = base_task.example
    quest = base_task.quest
    user = current_user
    form, result = check_from(user)
    table_names = user.get_table_names()
    return render_template('task/task.html', **result, table_names = table_names, name = name, description = description, instruction = instruction, example = example, quest = quest, task = task, form = form)

@bp.route("/finish/<task_id>")
def finish(task_id):
    task = Task.query.filter_by(task_id = task_id).first_or_404()
    if task.status == 1:
        user = current_user
        score, errors = ManagerTask.check(task_id = task_id, user = user)
        task_name = ManagerTask.get_task(task_id = task_id).name
        task.status = 2
        task.score = score
        db.session.commit()
        return render_template('task/finish.html', title = task_name, procent = task.score, errors = errors)
    else:
        return redirect(url_for('task.task', task_id = task_id))

@bp.route("/restart/<task_id>")
def restart(task_id):
    task = Task.query.filter_by(task_id = task_id).first_or_404()
    if task.status == 2:
        task.status = 0
        task.score = 0
        db.session.commit()
    return redirect(url_for('task.task', task_id = task_id))

@bp.route("/start/<task_id>")
def start(task_id):
    task = Task.query.filter_by(task_id = task_id).first_or_404()
    task_finish = Task.query.filter_by(status = 0).first()
    if not task_finish is None and task.id > task_finish.id: return redirect(url_for('task.task', task_id = task_finish.id))
    if task.status == 0:
        task.status = 1
        db.session.commit()
    return redirect(url_for('task.task', task_id = task_id))

# надо бы изменить страницу отображающую задание. Оставить название, оставить описание области применения и тд,
# и перенести текст задания на страничку консоли, ну и выводить там описание всех команд, но открывать его только по мере прохождения заданий.
