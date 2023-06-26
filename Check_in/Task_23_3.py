'''Наибольшее число, которое можно составить из массива чисел'''
lst = [9, 90, 92]
for i in range(len(lst)-1):
    for j in range(len(lst)-i-1):
        if str(lst[j]) + str(lst[j+1]) < str(lst[j+1]) + str(lst[j]):
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(''.join(map(str, lst)))