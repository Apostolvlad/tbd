from app.no_web.command import Command, Table

def add_row(*values, user = None, form = None):
    table = user.table()
    if table is None: return 'Таблица не выбрана'
    result = table.add_row(values = values)
    if result: return f'''Строка №{table.rows.count()} успешно добавлена!'''


Command.bind('add_row', add_row)