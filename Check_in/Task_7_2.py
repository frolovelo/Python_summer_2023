'''Шифр Цезаря'''
def cezar(text, n):
    lower_alp = 'abcdefghijklmnopqrstuvwxyz'
    upper_alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    t = ''
    n = n % 26
    for i in text:
        if i.isalpha():
            if i.islower():
                t += lower_alp[(lower_alp.find(i) + n) % 26]
            if i.isupper():
                t += upper_alp[(upper_alp.find(i) + n) % 26]
        else:
            t += i

    return t
print(cezar(input('Введите текст для зашифровки: '), int(input('Сдвиг: '))))