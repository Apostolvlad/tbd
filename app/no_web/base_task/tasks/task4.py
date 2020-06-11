from app.no_web.base_task import ManagerTask, Table
colomn_names = ('Название', 'Возраст', 'Местообитание', 'Размер')
def check(user):
    result_count = 100
    result = list()
    table = user.get_table('Животные')
    if table is None:
        result.append('Таблица с именем Животные не найдена!')
        result_count -= 100
    else:
        names = list()
        for col in table.cols: names.append(col.name)
        if len(colomn_names) != len(names):
            result.append(f'Количество столбцов не соотвествует заданию. {len(colomn_names)} != {len(names)}')
            result_count -= 40
        for name in colomn_names:
            if names.count(name) == 0: 
                result.append(f'Отсутствует столбец {name}')
                result_count -= 60 / len(colomn_names)
    return result_count, result

task = ManagerTask.add(
    name = """Добавление столбцов""",
    description = """Обычно таблицы представлены в виде столбцов, и строк. Поэтому в этом задании показано, как создаются столбцы.""",
    instruction = """Для добавления столбца используйте команду add_colomn('Название столбца 1', 'Название столбца 2')""",
    example = """add_colomn('Название столбца 1', 'Название столбца 2')""",
    quest = f"""Добавьте в таблицу Животные, такие столбцы: {', '.join(colomn_names)}""",
    check_func = check
)