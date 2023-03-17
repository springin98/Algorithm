import sys

N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
V = int(sys.stdin.readline().strip())

print(numbers.count(V))

#진짜 말도 안된다. count 함수가 있냐.

# 31256 KB
# 40ms