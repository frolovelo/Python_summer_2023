import re
text = input('Введите номера через пробел: ')
pattern = r'[ETOPAHKXCBMКЕНХВАРОСМT]'
print(*re.findall(rf"\b{pattern}\d\d\d{pattern}{pattern}[1]?78\b", text))
