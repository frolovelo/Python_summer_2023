'''re убираем зарезервированные слова из текста'''
import keyword
import re
t = 'hello mir False None, none as0 and break how you import?'

for search in keyword.kwlist:
    regex = rf'\b{search}\b'
    t = re.sub(regex, '<kw>', t)
print(t)
