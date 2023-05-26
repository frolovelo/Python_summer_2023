x = [int(i) for i in input('Введите числа через пробел: ').split()]
print([ind for ind, val in enumerate(x) if val == min(x)],
      [ind for ind, val in enumerate(x) if val == max(x)])