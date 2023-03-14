import sys

# num1, num2 = map(int, sys.stdin.readline().strip().split())
num1 = int(sys.stdin.readline().strip())
num2 = int(sys.stdin.readline().strip())

print(num1 * int(num2%10))
print(num1 * int(int(num2%100)/10))
print(num1 * int(num2/100))
print(num1 * num2)

#31256KB
#40ms