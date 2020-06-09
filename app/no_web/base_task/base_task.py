# это чтобы при создании новых заданий не импортировать отдельно Table
from app.models import Table, User
class BaseTask:
    def __init__(self, id, name, description, instruction, example, quest, check_func):
        self.id = id
        self.name = name # название задания
        self.description = description # описание навыка.
        self.instruction = instruction # инструкция
        self.example = example
        self.quest = quest # инструкция

        self.check_func = check_func

class ManagerTask:
    id = 0
    base_task = dict()
    base_check = dict()

    @classmethod
    def add(cls, **kwag):
        cls.id += 1
        t = BaseTask(cls.id, **kwag)
        cls.base_task.update({str(cls.id):t})
        return t

    @classmethod
    def check(cls, task_id, user):
        task = cls.get_task(task_id)
        try:
            return task.check_func(user = user)
        except Exception as e:
            return 0, (e,)
    
    @classmethod
    def get_task(cls, task_id):
        return cls.base_task.get(task_id)
    

#from tasks import *
