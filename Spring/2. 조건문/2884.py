import sys

H, M = map(int, sys.stdin.readline().strip().split())

if (M < 45) : 
    if(H == 0) : H = 24
    print(H-1, M+60-45)
else : 
    print(H, M-45)

#31256KB
#40ms