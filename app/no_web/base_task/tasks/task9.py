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
            result_count -= 50
        types = list()
        for row in table.rows:
            for e in row.items:types.append(e.item_type)
        r1 = 0
        r2 = 0
        r3 = 0
        if types.count(0) != 0: r1 = types.count(0) / len(types) * 100
        if types.count(1) != 0: r2 = types.count(1) / len(types) * 100
        if types.count(2) != 0: r3 = types.count(2) / len(types) * 100
        max = 0
        if r1 != r2 and r2 != r3 and r1 != r3:
            result.append(f'Процент строк цифрового типа = {r1}')
            result.append(f'Процент строк дробного типа = {r2}')
            result.append(f'Процент строк строкового типа = {r3}')
            result_count -= 50
        
    return result_count, result

task = ManagerTask.add(
    name = """Изменение значения строк""",
    description = """В этом задании показано, как можно изменить значение у строки.""",
    instruction = """Для изменения строки используйте команду set_row(номер строки, номер столбца, новое значение)""",
    example = """set_row(1, 1, 'New value')""",
    quest = f"""Сделайте половину строк с одним типом, а вторую половину с другим типом.""",
    check_func = check
)