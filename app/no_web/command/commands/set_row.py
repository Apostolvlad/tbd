from app.no_web.command import Command, Table

def set_row(index_row, index_col, value, user = None, form = None):
    errors = list()
    table = user.table()
    if table is None: errors.append('Таблица не выбрана')
    if not type(index_row) is int:  
        errors.append(f'Параметр = {index_row}, должен быть числом.')
    elif index_row <= 0: 
        errors.append(f'Параметр = {index_row}, должен быть больше нуля.')
    if not type(index_col) is int:  
        errors.append(f'Параметр = {index_col}, должен быть числом.')
    elif index_col <= 0: 
        errors.append(f'Параметр = {index_col}, должен быть больше нуля.')
    if len(errors): return errors
    result = table.set_row(index_row - 1, index_col - 1, value)
    if result:
        #form.table_id = 0
        return f'''Ячейка №{index_row}|{index_col} успешно изменена!'''
    else:
        return f'''Ячейка №{index_row}|{index_col} не существует!'''

Command.bind('set_row', set_row)