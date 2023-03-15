import sys

N = int(sys.stdin.readline().strip())

answer = []

for _ in range(1, int(N/4)+1) :
    answer.append('long')

answer.append('int')

print(' '.join(answer))

# 31256KB
# 60ms

# 다른 풀이 : 바로 출력해준다.

for _ in range(1, int(int(sys.stdin.readline().strip())/4)+1) :
    print('long', end=' ')

print('int')

# 31256 KB
# 40ms