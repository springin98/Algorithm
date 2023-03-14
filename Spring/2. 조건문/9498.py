import sys

score = int(sys.stdin.readline().strip())

if (90 <= score) and (score <= 100) : print('A')
elif (80 <= score) : print('B')
elif (70 <= score) : print('C')
elif (60 <= score) : print('D')
else : print('F')

#31256KB
#44ms