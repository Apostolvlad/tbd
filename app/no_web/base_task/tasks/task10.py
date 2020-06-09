from app.no_web.base_task import ManagerTask, Table

import random
table_colomns = ('Название', 'Вес', 'Тип', 'Возраст')
colomns1 = ('Обезьяна', 'Зубодёр', 'Кот', 'Лиса', 'Медведь','Баг')
colomns2 = (10, 20, 50, 100, 1000, 666)
colomns3 = ('Летающее', 'Травоядное', 'Человекопитающееся', 'Ползающее', 'Плавающее')
colomns4 = (1, 5, 9, 69, 33, 98)

symbol_errors = ('', '', '"', '+', 'ээ', 'Q')

symbol_errors1 = (' кило', ' килограмм', ' тонн', ' грамм')

symbol_errors2 = (' лет', ' годов', ' лун', ' зим')

def get_table_colomns():
    result = list()
    for name in table_colomns:
        new = list(name)#.split()
        i = random.randint(0, len(symbol_errors) - 1)
        new.insert(random.randint(0, len(new) - 1), symbol_errors[i])
        result.append(''.join(new))
    return result

def get_table_rows():
    result = list()
    for i in range(10):
        new = list()
        element1 = colomns1[random.randint(0, len(colomns1) - 1)]
        element2 = colomns2[random.randint(0, len(colomns2) - 1)]
        element3 = colomns3[random.randint(0, len(colomns3) - 1)]
        element4 = colomns4[random.randint(0, len(colomns4) - 1)]
        if random.randint(0, i + 1) == i: element1 += symbol_errors[random.randint(0, len(symbol_errors) - 1)]
        if random.randint(0, i + 1) == i: element2 = str(element2) + symbol_errors1[random.randint(0, len(symbol_errors1) - 1)]
        if random.randint(0, i + 1) == i: element3 += symbol_errors[random.randint(0, len(symbol_errors) - 1)]
        if random.randint(0, i + 1) == i: element4 = str(element4) + symbol_errors2[random.randint(0, len(symbol_errors2) - 1)]
        
        new.append(element1)
        new.append(element2)
        new.append(element3)
        new.append(element4)

        result.append(new)
    for e in range(5):
        if random.randint(0, e + 1) == e: result.insert(random.randint(0, 7), ['', '', '', ''])
        if random.randint(0, e + 1) == e: result.insert(random.randint(0, 7), ['+', '=', '-', '+'])
        if random.randint(0, e + 1) == e: result.insert(random.randint(0, 7), [3, 1, 5, 3])
    return result


def check(user):
    result_count = 100
    result = list()
    table = user.get_table('Тестовая таблица для задания 10')
    if table is None:
        result.append('Таблица с именем Тестовая таблица для задания 10 не найдена!')
        result_count -= 100
    else:
        if table.rows.count() != 13:
            result.append(f'Количество строк не соотвествует заданию. {table.rows.count()} != 13')
            result_count -= abs(table.rows.count() - 13) * 5
        for col in table.cols:
            if not symbol_errors.count(col):
                result.append(f'Название столбца не исправлено = {col}')
                result_count -= 10
        errors = 0
        for i2, row in enumerate(table.rows):
            for i, e in enumerate(row.items.all()):
                if e.item() == '': 
                    result.append(f'#{i2}|{i} - пустая ячейка')
                    errors += 1
                elif (i == 0 or i == 2) and e.item_type != 2: 
                    errors += 1
                    result.append(f'#{i2}|{i} - не является строкой = {e.item()}')
                else:
                    if (i == 1 or i == 3) and e.item_type != 0: 
                        errors += 1
                        result.append(f'#{i2}|{i} - не является числом = {e.item()}')
        result_count -= errors
        result.append(f'Всего ошибок в строках = {errors}')
    return result_count, result

task = ManagerTask.add(
    name = """Итоговое задание по пройденным функциям""",
    description = """Данное задание проверяет освоение работы с функциями для работы с таблицами.""",
    instruction = """Для получения таблицы введите команду create_test()""",
    example = """create_test()""",
    quest = f"""В этом задании требуется привести таблицу 'Тестовая таблица для задания 10' в порядок. Добавьте ещё несколько строк. Количество строк в таблице должно быть = 13.""",
    check_func = check
)