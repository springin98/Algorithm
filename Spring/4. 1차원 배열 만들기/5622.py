import sys

str = sys.stdin.readline().strip()
sum = len(str)*2

for i in range(len(str)) :
    if str[i] >= 'A' and str[i] <= 'C':
        sum += 1
    elif str[i] >= 'D' and str[i] <= 'F':
        sum += 2
    elif str[i] >= 'G' and str[i] <= 'I':
        sum += 3
    elif str[i] >= 'J' and str[i] <= 'L':
        sum += 4
    elif str[i] >= 'M' and str[i] <= 'O':
        sum += 5
    elif str[i] >= 'P' and str[i] <= 'S':
        sum += 6
    elif str[i] >= 'T' and str[i] <= 'V':
        sum += 7
    elif str[i] >= 'W' and str[i] <= 'Z':
        sum += 8
    
print(sum)

# 31256KB
# 40ms

# 코드가 더 간단해지는 방법
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i)+3
print(ret)
