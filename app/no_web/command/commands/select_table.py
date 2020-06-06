from app.no_web.command import Command, Table

def func(name_table, user, form):
    table_id = None
    for i, t in enumerate(user.tables):
        if t.name == name_table:
            table_id = i
            break
    if table_id is None:
        return f'''Таблица с {name_table} таким названием не существует!'''
    else:
        user.select_table(table_id)
        return f'''Таблица {name_table} успешно выбрана!'''

Command.bind('select_table', func)
