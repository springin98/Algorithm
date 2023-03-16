import sys
from collections import deque

N = int(sys.stdin.readline().strip())
dq = deque(i+1 for i in range(N))

for _ in range(N-1) :
    dq.popleft()
    dq.append(dq[0])
    dq.popleft()

print(dq[0])

# 51028KB
# 184ms

# 교재 풀이
# 다른 점은 while 문, dq.append 하는 것과 동시에 pop
dq = deque()
for i in range (1, int(sys.stdin.readline().strip())+1) :
    dq.append(i)

while len(dq) > 1 :
    dq.popleft()
    dq.append(dq.popleft())

print(dq.pop())

# 50936KB
# 196ms