from app.no_web.base_task import ManagerTask, Table

def check(user):
    result_count = 100
    result = list()
    table = user.get_table('Животные')
    if table is None:
        result.append('Таблица с именем Животные не найдена!')
        result_count -= 100
    else:
        if table.rows.count() != 6:
            result.append(f'Количество строк не соотвествует заданию. {table.rows.count()} != 6')
            result_count -= 100
    return result_count, result

task = ManagerTask.add(
    name = """Удаление строк""",
    description = """В этом задании показано, как удаляются строки.""",
    instruction = """Для удаления строки используйте команду del_row(номер строки)""",
    example = """del_row(3)""",
    quest = f"""Оставьте в таблице Животные 6 строк.""",
    check_func = check
)