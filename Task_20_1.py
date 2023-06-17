"""class заказ в кафе"""
from datetime import *

import colorama
from colorama import Fore, Style

colorama.init()

class Menu:
    def __init__(self, m):
        self.m = m


class Cafe:
    def __init__(self, name):
        '''Данные кафе'''
        self.name = name
        self.cash = 0
        self.card = 0
        self.customer_choice = []
        self.count = 0

    def search_menu(self, m, *prod):
        '''Поиск по меню'''
        res = []
        def search(product, m):
            for k, v in m.items():
                if k == product:
                    res.append((k, v))
                if isinstance(v, dict):
                    search(product, v)
        for product in prod:
            search(product, m)
        for product in prod:
            flag = False
            for i in res:
                if product == i[0]:
                    flag = True
            if not flag:
                print(Fore.RED + product + ', к сожалению закончился.' + Style.RESET_ALL)
        return res

    def client_choise(self, customer, menu, *products):
        '''Клиент выбирает заказ'''
        lst = self.search_menu(menu.m, *products)
        print(f'{customer.name}, итого к оплате: {sum(map(lambda x: x[1], lst))} руб.')
        customer.take_case(lst)

    def set_payments(self, customer, lst, pay):
        '''Оплата заказа'''
        sm = sum(map(lambda x: x[1], lst))
        def case(lst):
            t = ''
            for i in lst:
                t += f'{i[0]} - {i[1]} руб.\n'
            return t
        if pay >= sm:
            self.count += 1
            b = f'{"-"*20}\nЧек #{self.count}\nООО "{self.name}"\n{case(lst)}{datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")}\n{"-"*20}'
            customer.take_bill(b)
            return True
        else:
            print('Недостаточно средств')
            return False






class Client:
    def __init__(self, name, money_cash, money_card):
        '''Данные клиента'''
        self.name = name
        self.money_cash = money_cash
        self.money_card = money_card
        self.iwant = []
        self.bill = None

    def take_case(self, l):
        '''Получает список заказа'''
        self.iwant = l

    def pay(self, cafe, payment):
        '''оплачивает'''
        if payment == 'cash':
            payment = self.money_cash
            if cafe.set_payments(self, self.iwant, payment):
                self.money_cash -= payment
                print(Fore.GREEN + 'Оплата прошла успешно' + Style.RESET_ALL)
        elif payment == 'card':
            payment = self.money_card
            if cafe.set_payments(self, self.iwant, payment):
                self.money_card -= payment
                print(Fore.GREEN + 'Оплата прошла успешно' + Style.RESET_ALL)
        else:
            print(Fore.RED + 'Такого способа оплаты нет' + Style.RESET_ALL)


    def take_bill(self, bill):
        '''Получает чек'''
        self.bill = bill
        print(bill)




d = {'напиток': {'чай': {'черный чай': 100, 'зеленый чай': 120},
                 'кофе': {'капучино': 300, 'эспрессо': 150, 'латте': 350},
                 'вода': {'без газа': 50, 'газированная': 50}},
     'пирожное': {'торт': {'медовик': 130, 'сметанник': 120, 'тирамису': 250}, 'выпечка': {'cлойка': 40, 'язычок': 30}}}
menu = Menu(d)
cafe = Cafe('Рога и Копыта')
client = Client('Даниил', 400, 200)

cafe.client_choise(client, menu, 'тирамису', 'эспрессо', 'квас')
client.pay(cafe, 'cash')

print(cafe.name)
print(client.name, client.money_cash, client.money_card, client.bill)
# дописать отчётнгсть и всё
