import sys

cnt = 0
str = sys.stdin.readline().strip()

for i in range(len(str)) :
    if str[i] == " " :
        if str[i+1] != " " :
            cnt += 1
        
print(cnt+1)

# 틀림
# 다른 풀이
# 애초에 split() 함수를 사용하면 리스트 형식으로 [a, b, c] 이렇게 저장되는 걸 이용하면 된다.

print(len(sys.stdin.readline().strip().split()))
# 39196KB
# 52ms