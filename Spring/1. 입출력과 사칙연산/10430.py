import sys

inputNum = sys.stdin.readline().strip().split(' ')
A = int(inputNum[0])
B = int(inputNum[1])
C = int(inputNum[2])

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

#성능
#31256KB
#40ms