import sys

X = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())
total = 0

for _ in range(1, N+1) : 
    thing, amount = map(int, sys.stdin.readline().strip().split())
    total += (thing * amount)

print("Yes") if(X == total) else print("No")

# 31256 KB
# 40 ms