import re


# 1 вариант
def abre(t):
    return t[0].title()


text = 'Инстит точной          меХан оптИки'
a = re.sub(r'\b\w+\b', abre, text)
print(''.join(re.split(r'[a-zа-я ]+', a)))

# 2 вариант
a = re.findall(r'\b(\w)\w+\b', text)
print(''.join(a).upper())
