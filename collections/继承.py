# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     继承.py
   Author :        LiSen
   Date：          2018/8/2 21:10:
-------------------------------------------------
"""


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = '65kg'

    def talk(self):
        print 'person is talking'


class Chinese(Person):

    def __init__(self, name, age, language):
        # Person.__init__(self,name,age)
        super(Chinese, self).__init__(name, age)
        self.language = language

    def walk(self):
        print 'chinese is walking'

    def talk(self):
        print '%s is talking' % self.name


class SchoolMember(object):
    '''学习成员基类'''
    member = 0

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()

    def enroll(self):
        '注册'
        print('just enrolled a new school member [%s].' % self.name)
        SchoolMember.member += 1

    def tell(self):
        print('----%s----' % self.name)
        for k, v in self.__dict__.items():
            print(k, v)
        print('----end-----')

    def __del__(self):
        print('开除了[%s]' % self.name)
        SchoolMember.member -= 1


class Teacher(SchoolMember):
    '教师'

    def __init__(self, name, age, sex, salary, course):
        SchoolMember.__init__(self, name, age, sex)
        self.salary = salary
        self.course = course

    def teaching(self):
        print('Teacher [%s] is teaching [%s]' % (self.name, self.course))


class Student(SchoolMember):
    '学生'

    def __init__(self, name, age, sex, course, tuition):
        SchoolMember.__init__(self, name, age, sex)
        self.course = course
        self.tuition = tuition
        self.amount = 0

    def pay_tuition(self, amount):
        print('student [%s] has just paied [%s]' % (self.name, amount))
        self.amount += amount


if __name__ == '__main__':

    c = Chinese('bob', 20, 'chinese')
    c.talk()
    c.walk()
    print c.language
    print c.weight
