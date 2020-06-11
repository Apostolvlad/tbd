from app.no_web.command import Command, Table

def rename_colomn(index_col, name_col, user, form):
    errors = list()
    table = user.table()
    if table is None: errors.append('Таблица не выбрана')
    if not type(index_col) is int:  
        errors.append(f'Параметр = {index_col}, должен быть числом.')
    elif index_col <= 0: 
        errors.append(f'Параметр = {index_col}, должен быть больше нуля.')
    if not type(name_col) is str:  
        errors.append(f'Параметр = {name_col}, должен быть строкой.')
    if len(errors): return errors
    result = table.rename_colomn(index_col - 1, name_col)
    if result:
        #form.table_id = 0
        return f'''Колонка с индексом = {str(index_col)} успешно изменена!'''
    else:
        return f'''Колонка с индексом = {str(index_col)} не существует!'''

Command.bind('rename_colomn', rename_colomn)