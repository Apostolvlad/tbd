from app.no_web.command import Command, Table

def del_row(index, user, form):
    errors = list()
    table = user.table()
    if table is None: errors.append('Таблица не выбрана.')
    if not type(index) is int: 
        errors.append(f'Параметр = {index}, должен быть числом.')
    elif index <= 0:
        errors.append(f'Параметр = {index}, должен быть больше нуля.')
    if len(errors): return errors
    result = table.del_row(index - 1)
    if result:
        return f'''Строка №{index} успешно удалена!'''
    else:
        return f'''Строка №{index} не существует!'''
Command.bind('del_row', del_row)