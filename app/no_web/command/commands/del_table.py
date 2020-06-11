from app.no_web.command import Command, Table

def del_table(*kwag, user, form):
    errors = list()
    if user.table() is None: errors.append('''Таблица не выбрана!''')
    if len(kwag): errors.append('''Данная функция не принимает параметров!''')
    if len(errors): return errors
    name_table = user.table().name
    result = user.table().del_table()
    if result:
        #form.table_id = 0
        return f'''Таблица {name_table} успешно удалена!'''
        

Command.bind('del_table', del_table)