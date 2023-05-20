with open('text.txt', 'r', encoding='utf-8') as f:
    d = {}
    for i in f.read():
        i = i.lower()
        d[i] = d.get(i, 0) + 1
    d_sort = sorted(d, key=lambda x: (-d[x], x))
    c = 0
    for k in d_sort:
        if c == 10:
            break
        # Оставил repr для отображения /n и пробелов
        print(f'{repr(k):>4}-{d[k]}')
        c += 1
