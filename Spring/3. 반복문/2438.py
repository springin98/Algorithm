import sys

# for i in range(1, int(sys.stdin.readline().strip())+1) :
#     for j in range(1, i+1) :
#         print('*', end='')
#     print('\n', end='')

# 31256 KB
# 80ms

# 더 나은 방법
for i in range(1, int(sys.stdin.readline().strip())+1) :
    print('*' * i)

# 31256 KB
# 40ms