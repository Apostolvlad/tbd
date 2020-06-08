from app.no_web.command import Command, Table

def add_colomn(name_col, user, form):
    result = user.table()
    if result is None: return f'''Ошибка, таблица не выбрана!'''
    result.add_col(name = name_col)
    return f'''Столбец {name_col} успешно добавлен!'''


Command.bind('add_colomn', add_colomn)