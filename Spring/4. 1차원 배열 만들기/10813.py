import sys

N, M = map(int, sys.stdin.readline().strip().split())
baskets = [i for i in range(1, N+1)]

for _ in range (M) :
    i, j = map(int, sys.stdin.readline().strip().split())
    baskets[i-1], baskets[j-1] = baskets[j-1], baskets[i-1]

print(' '.join(map(str,baskets)))

# 31388KB
# 48 ms

# 틀린 이유 : join 은 str만 출력