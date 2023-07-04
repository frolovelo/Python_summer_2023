'''различия в строках'''
def vision(t1, t2):
    n = 0
    k = 0
    text = t1 if max([t1, t2], key=len) == t1 else t2
    for i in range(len(text)):
        try:
            if t1[i] != t2[i]:
                n += 1
            if t1[-i - 1] != t2[-i - 1]:
                k += 1
        except:
            n += 1
            k += 1

    return (False, t1, t2) if n > 1 and k > 1 else (True, t1, t2)


print(vision('abc', 'abc'))
print(vision('abc', 'abcd'))
print(vision('bc', 'abc'))
print(vision('axc', 'abc'))
print(vision('abc', 'acb'))
print(vision('abc', 'a'))
print(vision('', '  '))
print(vision('', ' '))
