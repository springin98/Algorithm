from sys import stdin

n = int(stdin.readline())
s = stdin.readline().rstrip()

dict = {}
for i in range(n):
    num = int(stdin.readline())
    dict[chr(ord('A')+i)] = num

stk = []

ops = ['+', '-', '*', '/']


def cal(op):
    global stk

    v2 = stk.pop()
    v1 = stk.pop()

    if op == '+':
        return v1 + v2
    elif op == '-':
        return v1 - v2
    elif op == '*':
        return v1 * v2
    elif op == '/':
        return v1 / v2


for c in s:
    if c in ops:
        res = cal(c)
        stk.append(res)
    else:
        stk.append(dict[c])

print(format(stk[0], '.2f'))
