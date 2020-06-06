from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import current_user, login_required
from app import db
from app.models import User, Table
from app.web.table import bp

@bp.route('/<table_id>', methods=['GET', 'POST'])
@login_required
def table(table_id):
    # сделать проверку, на доступ к таблице, если это твоя таблица, можно изменения делать, иначе нельзя...
    table = Table.query.filter_by(id = table_id).first_or_404()
    cols = table.get_cols()
    rows = table.get_rows()
    return render_template('table/table.html', title='Table',
                           cols = cols, rows = rows, table_title = table.name)

# сделать вывод вообще всех таблиц, всех юзеров...
@bp.route('all/<username>', methods=['GET', 'POST'])
@login_required
def all_table(username): #
    user = User.query.filter_by(username = username).first_or_404()
    rows = list()
    
    for table in user.tables:
        row = list()
        row.append((url_for('table.table', table_id = table.id), table.name))
        rows.append(row)

    return render_template('table/all_table.html', cols = ('Название',), rows = rows, table_title = 'Все таблицы')



