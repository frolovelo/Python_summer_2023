import colorama
from colorama import Fore, Style

colorama.init()

'''Результаты было решено учитывать статусом:
    1.None - задано домашнее задание
    2.Done - выполнено учеником
    3.Зачёт\Незачёт - в случае проверки учителем'''


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
                if self.homework[people.name][task] is not None:
                    self.homework[people.name][task] = status
                    people.take_homework(task, status=status)
                else:
                    print(Fore.RED + f'Учитель - будь внимательнее!\n{people.name} даже не начинал делать {task} - до "{status}" не дотягивает.' + Style.RESET_ALL)
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

    def complit_any_hometask(self, *info):
        '''Выполянет домашку по отдельной теме'''
        for i in info:
            if i in self.homework.keys():
                self.homework[i] = 'Done'
                self.send_homework(marIvanna)
            else:
                print(Fore.RED + f'Домашнего задания - {i} не задавали!' + Style.RESET_ALL)

    def complit_all_hometask(self):
        '''Выполянет всю домашку'''
        self.homework = {key: 'Done' for key in self.homework}
        self.send_homework(marIvanna)

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
marIvanna.set_homework(hometask[1], vasy)
marIvanna.set_homework(hometask[2:], pety)

print('То что было задано:', marIvanna.homework)

# Ученики выполняют домашнюю работу: Вася только 'Аннотации', а Петя всю, что задали (отправка на проверку предусмотрена сразу по выполнению)
vasy.complit_any_hometask('Аннотации')
pety.complit_all_hometask()

# Марьивановна решила проверить Генераторы и Декораторы у Пети и они оказались правильными - УРА!
marIvanna.check(pety, True, 'Генераторы', 'Декораторы')
# А вот Вася подкачал: Анотации сделал плохо, а ООП и вовсе не начинал делать:
marIvanna.check(vasy, False, 'ООП', 'Аннотации')

print('\nИтоговый результат:')
print('На руках у Учителя:', marIvanna.homework)
print(f'На руках у {vasy.name}: {vasy.homework}')
print(f'На руках у {pety.name}: {pety.homework}')
