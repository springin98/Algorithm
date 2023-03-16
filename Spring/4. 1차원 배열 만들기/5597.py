import sys

students = [0 for _ in range (30)]

for _ in range (28) :
    students[int(sys.stdin.readline().strip())-1] = 1

for i in range (30) :
    if students[i] == 0 :
        print(i+1, end=' ')

# 31256KB
# 40ms