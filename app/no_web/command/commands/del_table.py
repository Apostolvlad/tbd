from app.no_web.command import Command, Table

def del_table(name_table, user, form):
    result = Table.del_table(name_table, user)
    if result:
        #form.table_id = 0
        return f'''Таблица {name_table} успешно удалена!'''
    else:
        return f'''Таблица с {name_table} таким названием не существует!'''

Command.bind('del_table', del_table)