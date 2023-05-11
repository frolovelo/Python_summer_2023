n = int(input('Введите число: '))

lst = [0, 1]
f = 0
for i in range(n - 1):
    s = lst[i] + lst[i + 1]
    lst.append(s)
print(*lst[1:])
