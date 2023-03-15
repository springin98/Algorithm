import sys

T = int(sys.stdin.readline().strip())
results = []

for _ in range (0, T) :
    A, B = map(int, sys.stdin.readline().strip().split())
    results.append(A + B)

for i in results :
    print(i)

# 31256KB
# 44ms