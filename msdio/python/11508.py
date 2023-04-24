from sys import stdin

n = int(stdin.readline())
arr = [int(stdin.readline()) for i in range(n)]

arr.sort(reverse=True)

ans = 0
for i in range(n):
    if (i+1)%3 == 0:
        continue
    
    ans += arr[i]

print(ans)