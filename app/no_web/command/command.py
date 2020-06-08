import re
from app.models import Table, db
class Command:
    __command = dict()

    @classmethod
    def bind(cls, command, func): cls.__command.update({command:func}) 

    @classmethod
    def isfloat(cls, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
        return 2  

    @classmethod
    def process(cls, params):
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
    def pars_param(cls, text):
        result = re.findall(r"""('{1,1}.*?'{1,1})|([0-9]+|\.{0,1}[0-9]+) *?,{0,1} *?""", text)
        if result is None: return ()
        return cls.process(result)
    
    @classmethod
    def pars(cls, text):
        result = re.match(r'([A-Za-z_]*)\({1,1}', text) #\(.+?\)
        if result is None: return None, None
        return result.group(1), cls.pars_param(text = text[result.end():-1])
    
    @classmethod
    def check(cls, text, **kwag):
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
            db.session.commit()
            print(result)
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
