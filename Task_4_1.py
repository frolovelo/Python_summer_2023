from operator import *
d = {'+': add,
     '-': sub,
     '*': mul,
     '/': truediv}
t = input().split()
print(d[t[1]](int(t[0]), int(t[2])))