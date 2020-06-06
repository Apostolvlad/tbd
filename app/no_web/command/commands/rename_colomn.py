from app.no_web.command import Command, Table

def rename_colomn(index_col, name_col, user, form):
    result = user.table().rename_colomn(index_col, name_col)
    if result:
        #form.table_id = 0
        return f'''Колонка с индексом = {str(index_col)} успешно изменена!'''
    else:
        return f'''Колонка с индексом = {str(index_col)} не существует!'''

Command.bind('rename_colomn', rename_colomn)