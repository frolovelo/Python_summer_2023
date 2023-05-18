t = [i.strip() for i in input('Введите слова через запятую: ').split(',')]
print(sorted(t, key=lambda x: (-len(set(x)), x)))
