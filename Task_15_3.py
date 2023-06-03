import re


def find_phone_numbers(text):
    code1 = r'812'
    code2 = r'921'
    pat1 = r'\d{3}-\d{4}'
    pat2 = r'\d{3}-\d{2}-\d{2}'
    regex1 = rf'\B\+7\({code1}\){pat1}\b'
    regex2 = rf'\B\+7\({code1}\){pat2}\b'
    regex3 = rf'\B\+7\({code2}\){pat1}\b'
    regex4 = rf'\B\+7\({code2}\){pat2}\b'

    numb = re.findall(regex1, text) + re.findall(regex2, text) + re.findall(regex3, text) + re.findall(regex4, text)
    return numb


text = input('Введите номера через пробел: ')
phone_numbers = find_phone_numbers(text)
print(phone_numbers)