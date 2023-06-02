import re
text = input('Введите номера через пробел: ')
pattern = r'[ETOPAHKXCBM]'
print(*re.findall(rf"\b{pattern}\d\d\d{pattern}{pattern}78\b|\b{pattern}\d\d\d{pattern}{pattern}178\b", text))
