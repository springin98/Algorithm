import sys

while True :
    A, B = map(int, sys.stdin.readline().strip().split())
    if (A == 0 and B ==0) :
        break
    print(A+B)

# 31256KB
# 40ms