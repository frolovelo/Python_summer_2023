text = input()
s1, s2, s3 = set(), set(), set()
for i in text:
    if i.isalpha():
        s1 = s1 | set(i)
    elif i.isdigit():
        s2 = s2 | set(i)
    else:
        s3 = s3 | set(i)
print(*s1)
print(*s2)
print(*s3)