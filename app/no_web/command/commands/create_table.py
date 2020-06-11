from app.no_web.command import Command, Table

def create_table(name_table, user, form):
    if not type(name_table) is str: return f'Параметр = {name_table}, должен быть строкой.'
    if not user.get_table(name_table) is None: return f'''Таблица с {name_table} таким названием уже существует!'''
    result = Table.create_table(name_table, user)
    user.select_table(result.id)
    return f'''Таблица {name_table} успешно создана!'''
       

Command.bind('create_table', create_table)