import sys

for _ in range (int(sys.stdin.readline().strip())) :
    stk = []
    ans = 'YES'
    # 그 때마다 print 를 해주지 말고, YES, NO를 넣어주면 편하다.

    for c in sys.stdin.readline().strip() :
        if c == '(' :
            stk.append(c)
        else :
            # 여기서 스택의 길이를 검사하면 편해진다.
            if (len(stk) > 0) :
                # 맨 위를 뺀다.
                stk.pop()
            else :
                ans = 'NO'
    if(len(stk) > 0) :
        ans = 'NO'

    print(ans)

# 31256 KB
# 40ms