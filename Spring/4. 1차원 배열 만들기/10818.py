import sys

N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
min = numbers[0]
max = numbers[0]

for i in range (N) :
    if numbers[i] > max :
        max = numbers[i]
    if numbers[i] < min :
        min = numbers[i]

print(min, max)

# 1555744 KB
# 468ms

N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
print(min(numbers), max(numbers))
# 진짜 말도 안된다. max, min 함수까지 있어

# 150704 KB
# 400 ms