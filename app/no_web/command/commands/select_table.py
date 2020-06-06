from app.no_web.command import Command, Table

def func(name_table, user, form):
    result = Table.get_table(name_table, user)
    if result is None:
        return f'''Таблица с {name_table} таким названием не существует!'''
    else:
        user.select_table(result.id)
        return f'''Таблица {name_table} успешно выбрана!'''

Command.bind('select_table', func)
