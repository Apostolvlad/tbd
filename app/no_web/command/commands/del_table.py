from app.no_web.command import Command, Table

def del_table(user, form):
    if user.table() is None: return f'''Таблица не выбрана!'''
    
    name_table = user.table().name
    result = user.table().del_table()
    if result:
        #form.table_id = 0
        return f'''Таблица {name_table} успешно удалена!'''
        

Command.bind('del_table', del_table)