import sys

for _ in range (int(sys.stdin.readline().strip())) :
    str = sys.stdin.readline().strip()
    stack = []
    for i in range (len(str)) :
        if (str[i] == '(') :
            stack.append('(')
        elif (str[i] == ')') :
            if(str[len(stack)-1] == '(') :
                stack.pop(len(stack)-1)
            else :
                stack.append(')')
                break
    print("YES") if(stack == []) else print("NO")