import math

def solution(citations):
    citations.sort()
    
    cnt = len(citations)
    
    for i in range(cnt):
        if(citations[i] >= cnt-i):
            return cnt-i
        
    return 0