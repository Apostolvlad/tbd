from app.no_web.command import Command, Table

def add_colomn(*values, user, form):
    errors = list()
    result = user.table()
    if result is None: errors.append('''Ошибка, таблица не выбрана!''')
    if not len(errors):
        if type(values) is str: 
            result.add_col(name = name_col)
        elif type(values) is tuple:
            for e in values: 
                if type(e) is str:
                    result.add_col(name = e)
                else:
                    errors.append(f'Параметр = {e}, должен быть строкой.')
        else:
            errors.append(f'Не определён тип параметра = {values}')
    if len(errors): return errors
    return f'''Успешно!'''


Command.bind('add_colomn', add_colomn)