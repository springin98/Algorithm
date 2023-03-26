from sys import stdin

n = int(stdin.readline())
str = stdin.readline().rstrip()

sum = 0
for i in range(len(str)):
    sum += (ord(str[i]) - ord('a') + 1) * (31**i)
  
print(sum % 1234567891)
    