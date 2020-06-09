from datetime import datetime
from hashlib import md5
from time import time
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    table_id = db.Column(db.Integer) # выбранная таблица
    tables = db.relationship('Table', backref='user', lazy='dynamic')
    tasks = db.relationship('Task', backref='user', lazy='dynamic')
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_table_names(self):
        result = list()
        for t in self.tables:
            result.append(t.name)
        return result
    
    def select_table(self, table_id):
        self.table_id = table_id
        #db.session.commit()
    
    def table(self): return self.tables.filter_by(id = self.table_id).first()
    
    def get_table(self, name): return self.tables.filter_by(name = name).first()
    

'''
class TaskList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tasks = db.relationship('Task', backref='task_list', lazy='dynamic')
    name = db.Column(db.String(140)) # название задания
    description = db.Column(db.String(255)) # описание навыка.
    instruction = db.Column(db.String(255)) # инструкция
    example = db.Column(db.String(255))
    quest = db.Column(db.String(255)) # инструкция
    

'''

'''
    name = 'Создание таблицы'
    description = 'Таблица — это совокупность связанных данных, хранящихся в структурированном виде в базе данных. Она состоит из столбцов и строк.'
    instruction = 'Для создания таблицы, воспользуйтесь командой create_table, в которую надо передать название таблицы.'
    example = 'create_table("Тренажёр базы данных")'
    quest = 'Создайте таблицу с названием "Животные". Создайте ещё несколько таблиц с произвольным названием, минимум 2 таблицы.'

'''

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    task_id = db.Column(db.String(140))
    status = db.Column(db.Integer()) # статус выполнения 0 - не выполнено 1 - выполнено
    score = db.Column(db.Integer()) # процент выполнения задания.
    start_time = db.Column(db.DateTime, default = datetime.utcnow)
    finish_time = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Table {}>'.format(self.name)
    
    def get_rows(self):
        result = list()
        for row in self.rows: result.append(row.row())
        return result
    
    def get_cols(self):
        result = list()
        for col in self.cols: result.append(col.name)
        return result

class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(140)) # название таблицы
    cols = db.relationship('ColTable', backref='table', lazy='dynamic') 
    rows = db.relationship('RowTable', backref='table', lazy='dynamic') 
    #timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Table {}>'.format(self.name)
    
    def get_rows(self):
        result = list()
        for row in self.rows: result.append(row.row())
        return result
    
    def get_cols(self):
        result = list()
        for col in self.cols: result.append(col.name)
        return result
    
    def add_row(self, values = ()):
        row = RowTable(values = values)
        self.rows.append(row)
        #db.session.commit()
        return True # ИД добавленной строки
    
    def get_row(self, index):
        if index < self.rows.count(): return self.rows[index]
        return None

    def del_row(self, index):
        row = self.get_row(index)
        if row is None: return False
        row.del_row()
        return True
    
    def add_col(self, name):
        col = ColTable(name = name)
        self.cols.append(col)
        #db.session.commit()
        return True
    
    def get_col(self, index_col):
        if self.cols.count() > 0 and self.cols.count() > index_col: return self.cols[index_col]
        return False

    def del_col(self, index_col):
        col = self.get_col(index_col)
        if not col is None:
            return col.del_col()
        else:
            return False
    
    def rename_colomn(self, index_col, name):
        col = self.get_col(index_col)
        if col:
            col.name = name
            #db.session.commit()
        else:
            return False
        return True
    
    def set_row(self, index_row, index_col, value):
        row = self.get_row(index_row)
        if row is None: return False
        return row.set_value(index_col, value)
    
    @classmethod
    def get_table(cls, name, user):
        result = user.tables.filter_by(name = name).first()
        #result = db.session.query(User).filter(User.tables.name = name)
        return result

    @classmethod
    def create_table(cls, name, user):
        table = cls.get_table(name, user)
        if table is None:
            table = cls(name = name)
            user.tables.append(table)
            db.session.commit()
            return table
        else:
            return False

    def del_table(self):
        for e in self.rows:e.del_row()
        for e in self.cols:e.del_col()
        result = db.session.query(Table).filter(Table.name == self.name, Table.user_id == self.user_id).delete()#db.session.query(cls.user.tables).filter(cls.name == name).delete()#
        #db.session.commit()
        return result




class ColTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'))
    name = db.Column(db.String(255)) # название столбца
    
    def __repr__(self):
        return self.name
    
    def del_col(self):
        result = db.session.query(ColTable).filter(ColTable.name == self.name, ColTable.table_id == self.table_id).delete()#db.session.query(cls.user.tables).filter(cls.name == name).delete()#
        #db.session.commit()
        return True

class RowTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'))
    items = db.relationship('ItemTable', backref='row', lazy='dynamic') 
    
    def __repr__(self):
        return f'<RowTable {self.table_id}>'  

    def __init__(self, values):
        for value in values: self.add_item(value)

    def row(self):
        result = list()
        for item in self.items: result.append(item.item())
        return result
    
    def add_item(self, value):
        item = ItemTable(value)
        self.items.append(item)
        return True
    
    def get_item(self, index):
        if index < self.items.count(): return self.items[index]
        return None
    
    def set_value(self, index, value):
        item = self.get_item(index)
        if item is None: return False
        item.set_value(value)
        return True
    
    def del_row(self):
        for e in self.items:e.del_item()
        result = db.session.query(RowTable).filter(RowTable.id == self.id, RowTable.table_id == self.table_id).delete()#db.session.query(cls.user.tables).filter(cls.name == name).delete()#
        #db.session.commit()
        return True
    

class ItemTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    row_id = db.Column(db.Integer, db.ForeignKey('row_table.id'))
    item_type = db.Column(db.Integer())
    item_value = db.Column(db.String(200)) # значение

    def __repr__(self):
        return '<ItemTable {}>'.format(self.item_type, self.item_value)

    def __init__(self, item_value):
        self.set_value(item_value)
    
    def set_value(self, value):
        self.item_value = str(value)
        self.item_type = self.get_type(value)
        #db.session.commit()

    def get_type(self, value):
        if type(value) is int:#digit():
            return 0
        elif type(value) is float:
            return 1
        return 2      

    def item(self):
        result = self.item_value
        if self.item_type == 0:
            result = int(result)
        elif self.item_type == 1:
            result = float(result)
        elif self.item_type == 2:
            result = str(result)
        return result
    
    def del_item(self):
        result = db.session.query(ItemTable).filter(ItemTable.id == self.id, ItemTable.row_id == self.row_id).delete()#db.session.query(cls.user.tables).filter(cls.name == name).delete()#
        return True



@login.user_loader
def load_user(id):
    return User.query.get(int(id))