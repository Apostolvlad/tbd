from app.no_web.base_task import ManagerTask, Table
from .task4 import colomn_names
def check(user):
    result_count = 100
    result = list()
    table = Table.get_table('Животные', user)
    names = list()
    for col in table.cols: names.append(col.name)
    if len(colomn_names) != len(names):
        result.append(f'Количество столбцов не соотвествует заданию. {len(colomn_names)} != {len(names)}')
        result_count -= 50
    if names.count('Вес') == 0:
        result.append(f'Отсутствует столбец Вес')
        result_count -= 25
    if names.count('Размер') != 0:
        result.append(f'Столбец Размер не был изменён')
        result_count -= 25
    return result_count, result

task = ManagerTask.add(
    name = """Изменение столбцов""",
    description = """В данном задании вы научитесь изменять название, уже существующих, столбцов.""",
    instruction = """Для изменения названия используйте команду rename_colomn(номер столбца, 'Название колонки')""",
    example = """rename_colomn(2, 'Название колонки')""",
    quest = """Измените столбец Размер на Вес в таблице Животные.""",
    check_func = check
)