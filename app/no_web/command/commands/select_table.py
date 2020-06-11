from app.no_web.command import Command, Table

def func(name_table, user, form):
    if not type(name_table) is str: 
        return f'Параметр = {name_table}, должен быть строкой.'
    else:
        result = user.get_table(name_table)
        if result is None: return f'''Таблица с {name_table} таким названием не существует!'''
    user.select_table(result.id)
    return f'''Таблица {name_table} успешно выбрана!'''

Command.bind('select_table', func)
