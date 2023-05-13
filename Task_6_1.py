d = {
    'CM': 900,
    'M': 1000,
    'CD': 400,
    'D': 500,
    'XC': 90,
    'C': 100,
    'XL': 40,
    'L': 50,
    'IX': 9,
    'X': 10,
    'IV': 4,
    'V': 5,
    'I': 1
}
a = input()
print(a, end=' = ')
res = 0
while len(a) != 0:
    for key, val in d.items():
        if a.startswith(key):
            res += val
            a = a[len(key):]
            break
print(res)