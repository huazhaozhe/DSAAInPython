# -*- coding: utf-8 -*-
# @Author  : zhe
# @File    : person.py
# @Time    : 2018/04/27 21:06
# @Software: PyCharm

import datetime

class PersonTypeError(TypeError):
    pass

class PersonValueError(ValueError):
    pass


class Person:
    _num = 0

    def __init__(self, name, sex, birthday):
        if not isinstance(name, str):
            raise PersonTypeError('name must be str', name)
        if sex not in ('男', '女'):
            raise PersonValueError('sex must in "男" or "女"',sex)
        try:
            birth = datetime.date(*birthday)
        except:
            raise PersonValueError('Wrong date', birthday)
        self._name = name
        self._sex = sex
        self._birthday = birth
        self._age = datetime.date.today().year - self._birthday.year
        Person._num += 1
        self._id = Person._num

    def get_id(self): return self._id
    def get_name(self): return self._name
    def get_sex(self): return self._sex
    def get_birthday(self): return self._birthday
    def get_age(self): return datetime.date.today().year - self._birthday.year

    @classmethod
    def get_person_num(cls):
        return Person._num

    def set_birthday(self, birthday):
        try:
            birth = datetime.date(*birthday)
        except:
            raise PersonValueError('Wrong date', birthday)
        self._birthday = birth
        self._age = datetime.date.today().year - self._birthday.year

    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise PersonTypeError('set_name', new_name)
        self._name = new_name

    def __lt__(self, other):
        if not isinstance(other, Person):
            raise PersonTypeError('error other', other)
        return self.get_id() < other.get_id()

    def __str__(self):
        return ', '.join((
            self.get_id(),
            self.get_name(),
        ))

    def details(self):
        return ', '.join((
            'ID: ' + str(self.get_id()),
            'Name: ' + self.get_name(),
            'Sex: ' + self.get_sex(),
            'Birthday: ' + self.get_birthday().strftime('%Y-%m-%d'),
            'Age: ' + str(self.get_age()),
        ))

class Student(Person):

    _num = 0
    _id_num = 0

    @classmethod
    def _id_gen(cls):
        cls._id_num += 1
        Student._num += 1
        year = datetime.date.today().year
        return '1{:04}{:05}'.format(year, cls._id_num)

    def __init__(self, name, sex, birthday, department):
        Person.__init__(self, name, sex, birthday)
        self._department = department
        self._enroll_date = datetime.date.today()
        self._courses = {}
        self._id = Student._id_gen()

    def set_course(self, course_name):
        self._courses[course_name] = None

    def set_soure(self, course_name, score):
        if course_name in self._courses:
            self._courses[course_name] = score
        else:
            raise PersonValueError('没有选修这门课程')

    def set_department(self, department):
        self._department = department

    def get_scores(self):
        return [(course_name, score) for course_name,score in self._courses.items()]

    def get_score(self, course_name):
        if course_name in self._courses:
            return self._courses[course_name]
        else:
            raise PersonValueError('没有选修这门课')

    @classmethod
    def get_student_num(cls):
        return cls._num

    def details(self):
        return ', '.join(
            (
                Person.details(self),
                '入学日期：' + str(self._enroll_date),
                '院系：' + self._department,
                '课程记录：' + str(self.get_scores()),
            )
        )

class Staff(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls, birthday):
        cls._id_num += 1
        birth_year = datetime.date(*birthday).year
        return '0{:04}{:05}'.format(birth_year, cls._id_num)

    def __init__(self, name, sex, birthday, department, entry_date = None, position = None):
        super().__init__(name, sex, birthday)
        if entry_date:
            try:
                self._entry_date = datetime.date(*entry_date)
            except:
                raise PersonValueError('错误的日期格式')
        else:
            self._entry_date = datetime.date.today()
        self._salary = 1720
        self._department = department
        self._entry_age = datetime.date.today().year - self._entry_date.year
        self._position = position
        self._id = Staff._id_gen(birthday)

    def set_salary(self, salary):
        if type(salary) is int or type(salary) is float:
            if salary < 0:
                raise PersonValueError('工资小于0！')
            self._salary = salary
        else:
            raise PersonTypeError('错误，工作为整数或者小数')

    def set_department(self, department):
        self._department = department

    def set_position(self, position):
        self._position = position

    def get_department(self):
        return self._department

    def get_position(self):
        return self._position

    def get_salary(self):
        return self._salary

    def get_entry_date(self):
        return self._entry_date

    def get_entry_age(self):
        return self._entry_age

    def details(self):
        return ', '.join((
            super().details(),
            '入职日期：' + str(self._entry_date),
            '院系：' + self._department,
            '职位：' + self._position,
            '工资：' + str(self._salary),
            '工龄：' + str(self._entry_age),
        ))