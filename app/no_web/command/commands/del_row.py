from app.no_web.command import Command, Table

def del_row(index, user, form):
    table = user.table()
    if table is None: return 'Таблица не выбрана'
    result = table.del_row(index - 1)
    if result:
        #form.table_id = 0
        return f'''Строка №{index} успешно удалена!'''
    else:
        return f'''Строка №{index} не существует!'''
Command.bind('del_row', del_row)