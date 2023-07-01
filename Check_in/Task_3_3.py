'''Максимальные слова из списка'''
text = input().split()
m = len(text[0])
# находим максимум, можно было и так: len(max(text))
for i in text:
    if len(i) > m:
        m = len(i)
# находим все слова равные максимуму
lst = []
for i in text:
    if len(i) == m:
        lst.append(i)
print(*lst)

# функция однострочка
# print(*list(filter(lambda x: len(x) == len(max(text)), text)))
