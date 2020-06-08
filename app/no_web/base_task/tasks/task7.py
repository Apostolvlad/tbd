from app.no_web.base_task import ManagerTask, Table
def check(user):
    result_count = 100
    result = list()
    table = Table.get_table('Животные', user)
    if table.rows.count() != 10:
        result.append(f'Количество строк не соотвествует заданию. {table.rows.count()} != 10')
        result_count -= 40
    types = list()
    for row in table.rows:
        for e in row.items:types.append(e.item_type)
    r1 = types.count(0) / len(types) * 100
    r2 = types.count(1) / len(types) * 100
    r3 = types.count(2) / len(types) * 100
    max = 0
    if r1 > max:max = r1
    if r2 > max:max = r2
    if r3 > max:max = r3
    if max != 100:
        result.append(f'Процент строк одинакового типа = {max}')
        result_count -= (60 - 60 * (max / 100))
    
    return result_count, result

task = ManagerTask.add(
    name = """Добавление строк""",
    description = """В этом задании показано, как создаются строки.""",
    instruction = """Для добавления строки используйте команду add_row('строка', цифра и т.д.)""",
    example = """add_row('Страус', '1000 кг', 5, 'Зоопарк')""",
    quest = f"""Добавьте в таблицу Животные, 10 строк одного типа.""",
    check_func = check
)