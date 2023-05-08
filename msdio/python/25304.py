from sys import stdin

x = int(stdin.readline())
n = int(stdin.readline())

sum = 0
for _ in range(n):
    price, cnt = map(int, stdin.readline().split())

    sum += (price * cnt)

if sum == x:
    print('Yes')
else:
    print('No')
