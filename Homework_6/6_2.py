# task №6_2 by Kirill Peregud

from abc import ABC, abstractmethod

print('\n=========')
print('The program creates an abstract class of people, and classes of professions')
print('=========\n')


class Human(ABC):

    @abstractmethod
    def _name(self):
        pass

    @abstractmethod
    def _profession(self):
        pass

    @abstractmethod
    def age(self):
        pass

    @abstractmethod
    def city(self):
        pass

    @abstractmethod
    def education(self):
        pass

    @abstractmethod
    def gender(self):
        pass


class Manager(Human):

    _my_profession = 'manager'

    def __init__(self, my_name, my_age, my_city, my_education, my_gender):
        self._my_name = my_name
        self._my_age = my_age
        self._my_city = my_city
        self._my_education = my_education
        self._my_gender = my_gender

    def __repr__(self):
        return f'{self._profession}\n{self._name}'

    @property
    def _name(self):
        return f'Name -> {self._my_name}\n'
    
    @property
    def _profession(self):
        return f'Profession -> {self._my_profession}'

    @property
    def age(self):
        return f'Age -> {self._my_age}'

    @property
    def city(self):
        return f'City -> {self._my_city}'

    @property
    def education(self):
        return f'Education -> {self._my_education}'
    
    @property
    def gender(self):
        return f'Gender -> {self._my_gender}'


class Programmer(Manager):
    _my_profession = 'programmer'


class BusinessAnalyst(Manager):
    _my_profession = 'business analyst'


class Tester(Manager):
    _my_profession = 'tester'


def output_attr(human_class):
    result = [attr for attr in dir(human_class) if not (attr.startswith('__') or attr.startswith('_'))]
    return result


# Start of the program
manager = Manager('Vasya Ytkin', 42, 'Moscow', 'higher education', 'man')
programmer = Programmer('Ivan Belyi', 35, 'Minsk', 'higher education', 'man')
business_analyst = BusinessAnalyst('Volodya Mamkovich', 28, 'Mogilev', 'secondary education', 'man')
tester = Tester('Olga Garelaya', 32, 'Vitebsk', 'higher education', 'woman')

all_professions = [manager, programmer, business_analyst, tester]

for prof in all_professions:
    print(prof)
    for human in output_attr(prof):
        print(getattr(prof, human))
    print('\n=========\n')
