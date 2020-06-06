from app.no_web.base_task import ManagerTask, Table

def check(user):
    result_count = 100
    result = list()
    for t in user.tables:
        if t.id == user.table_id:
            if t.name != 'Животные':
                result.append('Таблица с именем Животные не выбрана!')
                result_count -= 100
            break
    return result_count, result

task = ManagerTask.add(
    name = """Выбор таблицы""",
    description = """Для того, чтобы получить возможность узнать чем заполнена ваша таблица, требуется выбрать её.""",
    instruction = """Для выбора таблицы используйте команду select_table('Название таблицы')""",
    example = """select_table('Тестовая таблица')""",
    quest = """Выберите таблицу с названием 'Животные' """,
    check_func = check
)