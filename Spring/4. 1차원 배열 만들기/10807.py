from sys import stdin

N = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))
V = int(stdin.readline())

print(numbers.count(V))

#진짜 말도 안된다. count 함수가 있냐.

# 31256 KB
# 40ms