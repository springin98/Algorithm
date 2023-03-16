import sys

cnt = 0
max = 0
maxCnt = 0

for i in range (9) :
    input =  int(sys.stdin.readline().strip())
    cnt += 1
    if (max < input) :
        max = input
        maxCnt = cnt

print(max)
print(maxCnt)

# 31256 KB
# 48 ms

# max, index 함수 사용
numbers = [int(sys.stdin.readline().strip()) for _ in range(9)]
print(max(numbers))
print(numbers.index(max(numbers)) + 1)

# 31256 KB
# 40ms