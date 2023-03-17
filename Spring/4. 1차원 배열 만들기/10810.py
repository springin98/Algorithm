import sys

N, M = map(int,sys.stdin.readline().strip().split())
buckets = [0 for _ in range(N)]

for _ in range(M) :
    i, j, k = map(int, sys.stdin.readline().strip().split())
    for z in range(i-1, j) :
        buckets[z] = k

for i in range(N) :
    print(buckets[i], end=' ')

# 31256KB
# 44ms

# 틀린 이유 : 출력을 [] 형식으로 함