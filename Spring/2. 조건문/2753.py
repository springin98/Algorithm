import sys

year = int(sys.stdin.readline().strip())

if (year%400 == 0) : print(1)
elif (year%4 == 0) : 
    if (year%100 != 0) :
        print(1)
    else : 
        print(0)
else : print(0)

#31256KB
#44ms