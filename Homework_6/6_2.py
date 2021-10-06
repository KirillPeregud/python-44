# task №6_2 by Kirill Peregud

from abc import ABC, abstractmethod

print('\n=========')
print('The program creates an abstract class of people, and classes of professions')
print('=========\n')


class Human(ABC):

    def __init__(self, my_name, my_gender, my_age, my_education, my_city):
        self.my_name = my_name
        self.my_gender = my_gender
        self.my_age = my_age
        self.my_education = my_education
        self.my_city = my_city

    @abstractmethod
    def name(self):
        pass
    
    @abstractmethod
    def gender(self):
        pass

    @abstractmethod
    def age(self):
        pass

    @abstractmethod
    def education(self):
        pass

    @abstractmethod
    def city(self):
        pass

class Manager(Human):

    my_profession = 'manager'
    @property
    def profession(self):
        return f'Profession -> {self.my_profession}'
    
    @property
    def name(self):
        return f'Name -> {self.my_name}'

    @property
    def gender(self):
        return f'Gender -> {self.my_gender}'
    
    @property
    def age(self):
        return f'Age -> {self.my_age}'

    @property
    def education(self):
        return f'Education -> {self.my_education}'
    
    @property
    def city(self):
        return f'City -> {self.my_city}'


class Programmer(Manager):
    my_profession = 'programmer'


class BusinessAnalyst(Manager):
    my_profession = 'business analyst'


class Tester(Manager):
    my_profession = 'tester'


def output_attr(human_class):
    res = [
        human_class.profession, human_class.name, human_class.gender,
        human_class.age, human_class.education, human_class.city
    ]
    # res1 = [a for a in dir(human_class) if not (a.startswith('__') or a.startswith('_'))]
    return res


manager = Manager('Vasya Ytkin', 'man', 42, 'higher education', 'Moscow')
programmer = Programmer('Ivan Belyi', 'man', 35, 'higher education', 'Minsk')
business_analyst = BusinessAnalyst('Volodya Mashkovich', 'man', 28, 'secondary education', 'Mogilev')
tester = Tester('Olga Garelaya', 'woman', 32, 'higher education', 'Vitebsk')

all_professions = [manager, programmer, business_analyst, tester]

for prof in all_professions:
    for human in output_attr(prof):
        print(human)
    print('\n=========\n')
