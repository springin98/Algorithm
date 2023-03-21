import sys

S = sys.stdin.readline().strip()

for i in range(ord('a'), ord('z')+1) :
    print(S.find(chr(i)), end=" ")
    
# 31256KB
# 60ms

# 틀린 이유 : range 할 때, +1을 안 해줬다. 그럼 1~122로 된다. 0~122로 해야 한다.