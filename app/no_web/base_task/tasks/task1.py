from app.no_web.base_task import ManagerTask, Table

def check(user):
    result_count = 100
    result = list()
    table = user.get_table('Животные')
    count = user.tables.count()
    if table is None: 
        result.append('Таблица с именем Животные не найдена!')
        result_count -= 40
    if count < 3: 
        result.append(f'Количество таблиц не соответствует заданию {count} < 3')
        result_count -= (3 - count) * 20
    return result_count, result

task = ManagerTask.add(
    name = """Создание таблицы""",
    description = """Таблица - это набор связанных данных.""",
    instruction = """Для создания таблицы используйте команду create_table('Название таблицы')""",
    example = """create_table('Тестовая таблица')""",
    quest = """Создайте таблицу с названием Животные. Создайте ещё, как минимум 2 таблицы с произвольным названием.""",
    check_func = check
)