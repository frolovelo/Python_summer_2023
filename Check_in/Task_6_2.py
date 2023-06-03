t1 = [i.strip() for i in input().split(',')]
t2 = [i.strip() for i in input().split(',')]
print(len(set(t1) & set(t2)))
print('Для проверки: ', set(t1) & set(t2))