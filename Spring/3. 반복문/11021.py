import sys

T = int(sys.stdin.readline().strip())

for i in range(1, T+1) :
    A,B = map(int, sys.stdin.readline().strip().split())
    print('Case #{}:'.format(i), A+B)

# 31256 KB
# 40ms