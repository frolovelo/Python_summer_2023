import colorama
from colorama import Fore, Style

colorama.init()

'''Результаты было решено учитывать статусом:
    None - задано домашнее задание
    Done - выполнено учеником
    Зачёт\Незачёт - в случае успешной проверки учителем'''


class DataHometask:
    def __init__(self, *info):
        '''Список всех домашних работ'''
        self.info = list(info)

    def __getitem__(self, item):
        return self.info[item]


class Teacher:
    def __init__(self):
        '''Хранит домашку {ученик:темы}'''
        self.homework = {}

    def set_homework(self, info: str | list, *pupil, status=None):
        '''Задаёт домашку'''
        for people in pupil:
            if isinstance(info, str):
                people.take_homework(info)
                self.homework[people.name] = self.homework.get(people.name, {})
                self.homework[people.name][info] = status
            else:
                for i in info:
                    people.take_homework(i)
                    self.homework[people.name] = self.homework.get(people.name, {})
                    self.homework[people.name][i] = status

    def get_homework(self, info, name):
        '''Получает домашку на проверку'''
        for k, v in info.items():
            if self.homework[name][k] != 'Зачёт':
                self.homework[name][k] = v

    def check(self, people, status: bool, *info):
        '''Зачёт/Незачёт'''
        status = 'Зачёт' if status else 'Незачёт'
        for task in info:
            if task in self.homework[people.name]:
                self.homework[people.name][task] = status
                people.take_homework(task, status=status)
            else:
                print(Fore.RED + f'{task} - не задавалось, поэтому и {status} некуда ставить...' + Style.RESET_ALL)


class Pupil:
    def __init__(self, name):
        '''Хранит домашку'''
        self.name = name
        self.homework = {}

    def take_homework(self, info, status=None):
        '''Получает домашку'''
        self.homework[info] = status

    def complit_any_hometask(self, info):
        '''Выполянет домашку по отдельной теме'''
        if info in self.homework:
            self.homework[info] = 'Done'
        else:
            print(Fore.RED + f'Домашнего задания - {info} не задавали!' + Style.RESET_ALL)

    def complit_all_hometask(self):
        '''Выполянет всю домашку'''
        self.homework = {key: 'Done' for key in self.homework}

    def send_homework(self, teacher):
        '''Отправляет домашку на проверку'''
        teacher.get_homework(self.homework, self.name)


# Все домашки
hometask = DataHometask('Аннотации', 'ООП', 'Генераторы', 'Декораторы')

# Создали учеников и учителя
marIvanna = Teacher()
vasy = Pupil('Василий')
pety = Pupil('Пётр')

# Задали домашку
marIvanna.set_homework(hometask[0], vasy, pety)
marIvanna.set_homework(hometask[2:], pety)

print('То что было задано:', marIvanna.homework)
print('У Петра информация по домашке:', pety.homework)
#
vasy.complit_any_hometask('Аннотации')
pety.complit_all_hometask()

pety.send_homework(marIvanna)
marIvanna.check(pety, True, 'Генераторы')
print()
print('То что было задано:', marIvanna.homework)
print('У Петра информация по домашке:', pety.homework)
