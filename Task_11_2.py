import csv
import openpyxl

with open(input('Введите исходный файл с расширением: '), encoding='utf-8') as f1:
    file_name_out = input('Введите результирующий файл с расширением: ')
    wb = openpyxl.Workbook()
    wb.save(file_name_out)
    ws = wb.active
    lst = [i for i in csv.reader(f1)]
    # Проверка первая строка имеет названия колонок или нет, например: ('Номер', 'Фамилия', 'Имя', 'Компания', 'Зарплата'):
    try:
        # Проверяем по столбцу Зарплата, он же последний[-1], если значение можно привести к int, то всё ок, ничего не меняем и бежим дальше
        av = int(lst[0][-1])
    except:
        # Если же там не числовое значение, значит мы добавляем в эксель первую строку с названием колонок и убираем из общего списка эту строку
        ws.append(lst[0])
        lst = lst[1:]
    s = 0

    for row in sorted(lst, key=lambda x: (x[3], x[1], x[2])):
        try:
            s += int(row[-1])
            ws.append(row)
        except:
            pass

    ws.append(['', '', '', 'Итого', s])
    wb.save(file_name_out)
    print('Работу завершил!')
