from app.no_web.command import Command, Table

def del_colomn(index_col, user, form):
    errors = list()
    table = user.table()
    if table is None:  errors.append('Таблица не выбрана')
    if not type(index_col) is int:  
        errors.append(f'Параметр = {index_col}, должен быть числом.')
    elif index_col <= 0: 
        errors.append(f'Параметр = {index_col}, должен быть больше нуля.')
    if len(errors): return errors
    result = table.del_col(index_col = index_col - 1)
    if result:
        #form.table_id = 0
        return f'''Колонка с индексом = {index_col} успешно удалена!'''
    else:
        return f'''Колонка с индексом = {index_col} не существует!'''

Command.bind('del_colomn', del_colomn)