import re

a = int(input('Введи двухзначное число для поиска: '))
pattern = rf"\s[0-{a//10}][0-{a%10}]?\b|\s[0-{(a//10)-1}]?\d\b"
text = '-123 -90 -80 -70 -45 -34 -23 -12 -9 -1 0 1 9 10 11 15 19 29 30 49 59 62 73 89 91 99 100 101 123 1000 32456'
print(', '.join([i.strip() for i in re.findall(rf"{pattern}", text)]))