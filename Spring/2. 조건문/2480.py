import sys

num1, num2, num3 = map(int, sys.stdin.readline().strip().split())

if (num1 == num2) and (num2 == num3) :
    print(10000 + num1*1000)
elif (num1 != num2) and (num2 != num3) and (num1 != num3) :
    if (num1 > num2) and (num1 > num3) :
        print(num1*100)
    elif (num2 > num1) and (num2 > num3) :
        print(num2*100)
    else :
        print(num3*100)
else :
    if (num1 == num2) :
        print(1000 + num1*100)
    elif (num1 == num3) :
        print(1000 + num1*100)
    else :
        print(1000 + num2*100)

# 31256KB
# 44ms

#더 나은 방법

num1, num2, num3 = map(int, sys.stdin.readline().strip().split())

if (num1 == num2 == num3)  :
    print(10000 + num1*1000)
elif (num1 == num2) :
    print(1000 + num1*100)
elif (num2 == num3) : 
    print(1000 + num2*100)
elif (num1 == num3) :
    print(1000 + num1*100)
else :
    print(100*max(num1, num2, num3))

# 31256KB
# 60ms