count = 0
i = int(input())
s = i
while s > 0:
    s = int(input())
    i += s
    count += 1
print(i/count if count != 0 else i)