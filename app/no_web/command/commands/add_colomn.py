from app.no_web.command import Command, Table

def add_colomn(name_col, user, form):
    result = user.table().add_col(name = name_col)
    if result:
        #form.table_id = 0
        return f'''Столбец {name_col} успешно добавлен!'''
    else:
        return f'''Ошибка, таблица не выбрана!'''

Command.bind('add_colomn', add_colomn)