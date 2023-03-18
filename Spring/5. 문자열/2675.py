import sys

T = int(sys.stdin.readline().strip())

for _ in range(T) :
    R, S = sys.stdin.readline().strip().split()
    R = int(R)
    for i in range(0, len(S)) :
        print(S[i]*R, end="")
    print()

# 31256KB
# 40ms