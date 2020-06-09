import re
from app.models import Table, db
class Command:
    __command = dict() # словарь в котором хранятся команды и функции которые должны выполнятся при их использовании

    @classmethod
    def bind(cls, command, func): cls.__command.update({command:func}) # метод класса, для добавления новых команд и функции.

    @classmethod
    def isfloat(cls, value): # функция для проверки типа данных - Дробные числа.
        try:
            float(value)
            return True 
        except ValueError:
            return False

    @classmethod
    def process(cls, params): # функция для преобразования полученных параметров в требуемые типы данных.
        result = list()
        for e in params: result.extend(list(e))
        result2 = list()
        for e in result: 
            if e != '':
                if e.isdigit():
                    result2.append(int(e))
                elif cls.isfloat(e):
                    result2.append(float(e))
                else:
                    result2.append(e.replace("'", ''))
        return result2

    @classmethod
    def pars_param(cls, text): # функция для извлечения параметров из строки параметров.
        result = re.findall(r"""('{1,1}.*?'{1,1})|([0-9]+|\.{0,1}[0-9]+) *?,{0,1} *?""", text)
        if result is None: return ()
        return cls.process(result)

    @classmethod
    def pars(cls, text): # функция для извлечения тела функции и параметров функции.
        result = re.match(r'([A-Za-z_]*)\({1,1}', text) 
        if result is None: return None, None
        return result.group(1), cls.pars_param(text = text[result.end():-1])

    @classmethod
    def check(cls, text, **kwag): # функция для определения полученной команды, и её выполнения.
        command, params = cls.pars(text)
        if command is None: return f"""Команда не определена!\nТекст = {text}"""
        func = cls.__command.get(command)
        if func is None: return f"""Команда не правильно написана!\nКоманда = {command},\nПараметры = {params}."""
        try:
            if len(params) and len(kwag):
                result = func(*params, **kwag)
            elif len(params):
                result =  func(*params)
            elif len(kwag):
                result = func(**kwag)
            else:
                result = funс()
            db.session.commit() # после выполнения команды, сохраняем изменения в базе данных.
            return result
        except Exception as e:
            return f"""Ошибка = {e}!\nКоманда = {command},\nПараметры = {params}."""






def test(*kwag, num1 = 0, num2 = 0):
    print(*kwag, num1, num2)
    return 'OK'

if __name__ == "__main__":
    c = Command()
    c.bind('create_table', test)
    result = c.check("""rename_colomn(2, 'Название таблицы')""") #"test"
    print(result)
