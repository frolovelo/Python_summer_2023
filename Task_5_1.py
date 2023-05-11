# треугольник Паскаля
n = 10
# Решение при помощи функции zip
# r = [1]
# for i in range(n):
#     print(*r)
#     res1 = [0] + r
#     res2 = r + [0]
#     r = [sum(i) for i in zip(res1, res2)]

r = [1]
for i in range(n):
    print(*r)
    res = [0] + r + [0]  # 0,1,0 --> 0,1,1,0...
    n = []
    for k in range(0, len(res) - 1):
        s = res[k] + res[k + 1]  # 0+1, 1+0 --> 0+1,1+1,1+0...
        n.append(s)
    r = n
