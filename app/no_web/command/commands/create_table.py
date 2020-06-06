from app.no_web.command import Command, Table

def create_table(name_table, user, form):
    result = Table.create_table(name_table, user)
    if result:
        user.select_table(result)
        return f'''Таблица {name_table} успешно создана!'''
    else:
        return f'''Таблица с {name_table} таким названием уже существует!'''

Command.bind('create_table', create_table)