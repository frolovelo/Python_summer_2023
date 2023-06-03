t = input('Введите строку').upper()
new = ''
i = 0
while i < len(t)-1:
    if t[i] + t[i+1] == 'АГ' or t[i] + t[i+1] == 'ГА':
        new += t[i+1] + t[i]
        i += 2
    elif t[i] + t[i+1] == 'ТЦ' or t[i] + t[i+1] == 'ЦТ':
        new += t[i] + 'АГ' + t[i+1]
        i += 2
    else:
        new += t[i]
        i += 1
if i == len(t) - 1:
    new += t[-1]
print(new)