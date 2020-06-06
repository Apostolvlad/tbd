from app.no_web.base_task import ManagerTask, Table

def check(user):
    result_count = 100
    result = list()
    table = Table.get_table('Животные', user)
    count = user.tables.count()
    if table is None: 
        result.append('Таблица с именем Животные не найдена!')
        result_count -= 50
    if count != 1: 
        result.append(f'Количество таблиц не соответствует заданию {count} != 1')
        result_count -= 50
    return result_count, result

task = ManagerTask.add(
    name = """Удаление таблицы""",
    description = """Удаление таблицы довольно важная возможность. Когда вы начнёте реогранизовывать вашу базу данных, некоторые таблицы понадобиться удалить из - за того, что данные которые они хранили, перестали быть нужны, или же будут хранится в другой таблице.""",
    instruction = """Для удаления таблицы используйте команду del_table('Название таблицы')""",
    example = """del_table('Тестовая таблица')""",
    quest = """Удалите ВСЕ таблицы, кроме таблицы с названием Животные.""",
    check_func = check
)