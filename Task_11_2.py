import csv
import openpyxl

with open(input('Введите исходный файл с расширением: '), encoding='utf-8') as f1:
    file_name_out = input('Введите результирующий файл с расширением: ')
    wb = openpyxl.Workbook()
    wb.save(file_name_out)
    ws = wb.active
    ws.append(['Номер', 'Фамилия', 'Имя', 'Компания', 'Зарплата'])
    s = 0

    for row in sorted(csv.reader(f1), key=lambda x: (x[3], x[1], x[2])):
        try:
            s += int(row[-1])
            ws.append(row)
        except:
            pass

    ws.append(['', '', '', 'Итого', s])
    wb.save(file_name_out)

    print('Работу завершил!')
