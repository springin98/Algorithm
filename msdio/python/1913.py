from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())

arr = [[0]*n for i in range(n)]
cur = n*n

i, j = 0, 0
left, right, up, down = 0, 0, 1, 0
mid = (n+1)//2
while cur > 0:
    arr[i][j] = cur
    cur -= 1
        
    if right:
        if j+1 >= n or arr[i][j+1]:
            left, right, up, down = 0, 0, 0, 1
            i -= 1
        else:
            j += 1
    elif left:
        if j-1 < 0 or arr[i][j-1]:
            left, right, up, down = 0, 0, 1, 0
            i += 1
        else:
            j -= 1
    elif down:
        if i-1 < 0 or arr[i-1][j]:
            left, right, up, down = 1, 0, 0, 0
            j -= 1
        else:
            i -= 1
    elif up:
        if i+1 >= n or arr[i+1][j]:
            left, right, up, down = 0, 1, 0, 0
            j += 1
        else:
            i += 1
            
ay, ax = -1, -1
for i in range(n):
    for j in range(n):
        if arr[i][j] == m:
            ay, ax = i, j

for a in arr:
    print(*a)
print(ay+1, ax+1)
