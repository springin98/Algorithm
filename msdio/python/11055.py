from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

dp = [0]*1001

for i in range(n):
    cur = arr[i]
    dp[cur] = max(dp[:cur]) + cur

print(max(dp))
