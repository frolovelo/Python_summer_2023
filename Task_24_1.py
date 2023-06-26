'''Bubble sorting'''
def bubble(t):
    ln = len(t)
    for i in range(ln - 1):
        for j in range(ln - i - 1):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]
    return t


t = [100, 1, 24, 35, 2, 43, 10, 0]
print(bubble(t))
