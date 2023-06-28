'''CamelCase from string'''

def camel(t):
    return ''.join([i.title() for i in t.split()])

t = 'caMel CasE fOrEvEr'
print(camel(t))