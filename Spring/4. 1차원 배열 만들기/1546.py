import sys

N = int(sys.stdin.readline().strip())
score = list(map(int, sys.stdin.readline().strip().split()))
maxScore = max(score)
sum = 0

for i in range(N) :
    score[i] = score[i]/maxScore*100
    sum += score[i]

print(sum/N)

# 31256 KB
# 40ms