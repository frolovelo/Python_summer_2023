'''type для создания класса'''


def dis(self):
    for k, v in self.__dict__.items():
        print(k, '-', v)


Pet = type('Pet', (), {'dis': dis})
my_pet = Pet()
my_pet.name = 'Tom'
my_pet.age = 192
my_pet.dis()
