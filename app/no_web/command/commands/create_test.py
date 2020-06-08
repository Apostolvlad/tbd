from app.no_web.command import Command, Table
from app.no_web.base_task import task10
from .del_table import del_table
from .create_table import create_table
from .add_colomn import add_colomn
from .add_row import add_row

def create_test(user, form):
    table = user.get_table('Тестовая таблица для задания 10')
    if not table is None: table.del_table()

    create_table('Тестовая таблица для задания 10', user, form)

    for name in task10.get_table_colomns(): add_colomn(name, user, form)
    for elements in task10.get_table_rows(): add_row(*elements, user = user, form = form)

    #user.select_table(result)
    if True: return f'''Таблица Тестовая таблица для задания 10 успешно создана!'''
    

#create_test()

Command.bind('create_test', create_test)