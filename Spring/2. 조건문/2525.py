import sys

H, M = map(int, sys.stdin.readline().strip().split())
cookTime = int(sys.stdin.readline().strip())

H = H + int((M + cookTime)/60)
M = (M + cookTime)%60

if (H >= 24) :
    H = H-24

print(H, M)

#31256KB
#40ms