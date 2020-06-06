from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import current_user, login_required
from app import db
from app.web.console.forms import CommandForm
from app.models import User, Table
from app.web.console import bp
from app.no_web.command import Command

def check_from(user):
    form = CommandForm()
    if form.validate_on_submit():
        command = form.command.data
        print(command)
        result = Command.check(command, user = user, form = form)
        print(result)
        flash(result)
        form.command.data = ''
        #return redirect(url_for('table.table', table_id = table_id))
    elif request.method == 'GET':
        pass
    table = user.table() #Table.query.filter_by(id = user.table_id).first()
    if table is None:
        table_title = 'Таблица не выбрана'
        cols = {}
        rows = {}
    else:
        cols = table.get_cols()
        rows = table.get_rows()
        table_title = table.name
    result = dict()
    result.update({'table_title': table_title})
    result.update({'cols': cols})
    result.update({'rows': rows})
    return form, result

@bp.route('/', methods=['GET', 'POST'])
@login_required
def console(): #
    user = current_user
    form, result = check_from(user)
    return render_template('console/console.html', **result, form = form)








