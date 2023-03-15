import sys

sum = []

for _ in range (int(sys.stdin.readline().strip())) :
    A, B = map(int, sys.stdin.readline().strip().split())
    sum.append(A+B)

print('\n'.join(map(str, sum)))

# 146367KB
# 1132ms

# join 은 str 형만 반환

for _ in range (int(sys.stdin.readline().strip())) :
    A, B = map(int, sys.stdin.readline().strip().split())
    print(A+B)

# 31256KB
# 1360ms