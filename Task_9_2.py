vowels = ('ауоыиэяюёе')
def mask(word):
    return [i for i in range(len(word)) if word[i] in vowels]

etalon = mask(input('Введите эталон: '))
lst = []
for _ in range(int(input('Кол-во слов для проверки: '))):
    t = input('Введите слово для проверки: ')
    if etalon == mask(t):
        lst.append(t)
print(*lst, sep='\n')