from collections import deque

def solution(numbers, k):
    dq = deque(numbers)
    cnt = 1
    while cnt != k :
        dq.append(dq.popleft())
        dq.append(dq.popleft())
        cnt += 1
        
    return dq[0]