t1 = input()
t2 = input()
d1 = {}
d2 = {}
text_del = '1234567890 -!?;:,."*()%$#@/&'
for i in t1:
    if i in text_del:
        t1 = t1.replace(i, '')
for i in t2:
    if i in text_del:
        t2 = t2.replace(i, '')
for i in t1:
    d1[i] = d1.get(i, 0) + 1
for i in t2:
    d2[i] = d2.get(i, 0) + 1
print(True if d1 == d2 else False)
print('Для проверки:')
print(*sorted(t1), sep='')
print(*sorted(t2), sep='')