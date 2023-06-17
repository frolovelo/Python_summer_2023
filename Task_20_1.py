"""class заказ в кафе"""


class Menu:
    def __init__(self, m):
        self.m = m


class Cafe:
    def __init__(self, name):
        self.name = name
        self.cash = 0
        self.card = 0
        self.customer_choice = []

    def search_menu(self, m, *prod):
        res = []
        def search(product, m):
            for k, v in m.items():
                if k == product:
                    res.append((k, v))
                if isinstance(v, dict):
                    search(product, v)
        for product in prod:
            search(product, m)
        return res

    def client_choise(self, customer, menu, *products):
        print(f'{customer.name}, проверьте ваш заказ:')
        for i in self.search_menu(menu.m, *products):
            print(*i, sep=' - ', end=' руб.\n')



class Client:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.iwant = []
        self.bill = None

    def take_bill(self, bill):
        self.bill = bill


d = {'напиток': {'чай': {'черный чай': 100, 'зеленый чай': 120},
                 'кофе': {'капучино': 300, 'эспрессо': 150, 'латте': 350},
                 'вода': {'без газа': 50, 'газированная': 50}},
     'пирожное': {'торт': {'медовик': 130, 'сметанник': 120, 'тирамису': 250}, 'выпечка': {'cлойка': 40, 'язычок': 30}}}
menu = Menu(d)
cafe = Cafe('Рога и Копыта')
client = Client('Даниил', 500)

cafe.client_choise(client, menu, 'тирамису', 'эспрессо')
