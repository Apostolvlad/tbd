from app.no_web.base_task import ManagerTask, Table

def check(user):
    result_count = 100
    result = list()
    table = user.table() # тут надо таблицу Животные искать...
    names = table.get_cols()
    if 1 != len(names):
        result.append(f'Количество столбцов не соотвествует заданию. 1 != {len(names)}')
        result_count -= 100
    return result_count, result

task = ManagerTask.add(
    name = """Удаление столбца""",
    description = """В этом задании вы получите опыт в удалении столбцов.""",
    instruction = """Для удаления столбца используйте команду del_colomn(номер столбца)""",
    example = """del_colomn(1)""",
    quest = """Оставьте только 1 столбец в таблице Животные.""",
    check_func = check
)