tree = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7), (7, 8)]
target_value = int(input('Введите число для поиска: '))

# Сформировал словарь
d = {}
for parent, child in tree:
    if parent not in d:
        d[parent] = []
    d[parent].append(child)


# Рекурсия на поиск кол-ва шагов - неэффективная))
def rec(d, target_value, steps=0):
    if target_value not in d.keys() and all(True if target_value not in i else False for i in d.values()):
        return f'Value {target_value} is not definied'
    for k, v in d.items():
        if target_value in v:
            steps += 1
            return rec(d, k, steps)
    return f'Need {steps} steps'


print(rec(d, target_value))
