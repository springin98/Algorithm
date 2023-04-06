from collections import deque

def solution(A, B):
    dq_A = deque(A)
    cnt = 0
    
    while ''.join(dq_A) != B :
        dq_A.rotate(1)
        cnt += 1
        if cnt-1 == len(A) :
            return -1

    return cnt