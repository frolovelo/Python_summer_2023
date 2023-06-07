def deco(func):
    def wrapper(*args, **kwargs):
        lst = []
        val = func(*args, **kwargs)
        lst.extend([i.upper() for i in val if type(i) == str])
        return lst
    return wrapper


@deco
def test(t):
    return t


print(test([1, 'to be or not to be', ['3', 1], {'4': '5'}, 'a hero']))
