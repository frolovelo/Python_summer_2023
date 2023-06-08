def deco(func):
    def wrapper(*args, **kwargs):
        lst = []
        func(*args, **kwargs)
        [lst.append(i) for i in args if isinstance(i, str)]
        [lst.append(i) for i in kwargs.values() if isinstance(i, str)]
        return lst
    return wrapper


@deco
def test(*args, **kwargs):
    return


print(test(1, 'to be or not to be', ['3', 1], {'4': '5'}, 'a hero', my='Даниил', brain='просто не понял задания...', test=5))
