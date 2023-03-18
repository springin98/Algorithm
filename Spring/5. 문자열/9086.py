import sys

N = int(sys.stdin.readline().strip())

for _ in range(N) :
    str = sys.stdin.readline().strip()
    print(str[0]+str[-1])
    
# 틀린 이유 : 공백없이 출력하려면 print(str[0], str[-1], end="") 인 줄 알았지만 그러면 줄바꿈이 안된다.

# 31256 KB
# 40ms