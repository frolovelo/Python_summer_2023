'''() правильные скобки'''
def bol(t):
    c = 0
    for i in t:
        if i == '(':
            c += 1
        elif i == ')':
            c -= 1
        if c < 0:
            return False
    return False if c else True


text = input('Введите скобочки:')
print(bol(text))
