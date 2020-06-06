from app.no_web.command import Command, Table

def del_colomn(index_col, user, form):
    result = user.table().del_col(index_col = index_col)
    if result:
        #form.table_id = 0
        return f'''Колонка с индексом ={str(index_col)} успешно удалена!'''
    else:
        return f'''Колонка с индексом ={str(index_col)} не существует!'''

Command.bind('del_colomn', del_colomn)