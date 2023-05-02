from sys import stdin

n, l = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

arr.sort()

cur_end = 0
cnt = 0
for a in arr:
    if cur_end < a:
        cnt += 1
        cur_end = a+l-1

print(cnt)