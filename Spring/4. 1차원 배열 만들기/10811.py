import sys

N, M = map(int, sys.stdin.readline().strip().split())
baskets = [i+1 for i in range(N)]

for _ in range(M) :
    i, j = map(int, sys.stdin.readline().strip().split())
    if (j-i) == 1 :
        runCnt = 1
    else :
        runCnt = int((j-i)/2)+1
    for k in range(runCnt) :
        baskets[i+k-1], baskets[j-k-1] = baskets[j-k-1], baskets[i+k-1]

print(' '.join(map(str, baskets)))

# 31388 KB
# 44ms