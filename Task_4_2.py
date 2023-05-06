n = int(input())
mx, my = 1, 0
x, y = 0, 0
arr = [[0] * n for _ in range(n)]
for i in range(1, n**2+1):
    arr[x][y] = i
    nx, ny = x+mx, y+my
    if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
        x, y = nx, ny
    else:
        mx, my = - my, mx
        x, y = x + mx, y + my
for x in list(zip(*arr)):
    print(*x)