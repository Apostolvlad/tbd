from app.no_web.command import Command, Table

def set_row(index_row, index_col, value, user = None, form = None):
    table = user.table()
    if table is None: return 'Таблица не выбрана'
    result = table.set_row(index_row - 1, index_col - 1, value)
    if result:
        #form.table_id = 0
        return f'''Ячейка №{index_row}|{index_col} успешно изменена!'''
    else:
        return f'''Ячейка №{index_row}|{index_col} не существует!'''

Command.bind('set_row', set_row)