import sys

for i in range(1, int(sys.stdin.readline().strip())+1) :
    A, B = map(int, sys.stdin.readline().strip().split())
    print(f'Case #{i}: {A} + {B} = {A+B}')

# 31256KB
# 40ms