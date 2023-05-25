import csv
import openpyxl

with open(input('Введите исходный файл с расширением: '), encoding='utf-8') as f1:
    file_name_out = input('Введите результирующий файл с расширением: ')
    wb = openpyxl.Workbook()
    wb.save(file_name_out)
    ws = wb.active
    lst = ['номер', 'фамилия', 'имя', 'компания', 'зарплата']
    ws.append(lst)
    s = 0

    for row in sorted(csv.reader(f1), key=lambda x: (x[3], x[1], x[2])):
        if row != lst:
            ws.append(row)
            s += int(row[-1])

    ws.append(['', '', '', 'Итого', s])
    wb.save(file_name_out)

    print('Работу завершил!')
