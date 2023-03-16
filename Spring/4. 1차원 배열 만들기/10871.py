import sys

N, X = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))

for i in range (N) :
    if A[i] < X :
        print(A[i], end=" ")

# 32267KB
# 48ms