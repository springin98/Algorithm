import heapq

def solution(k, m, score):
    hq = []

    for s in score:
        heapq.heappush(hq, -s)
    
    ans = 0
    for _ in range(len(score) // m):
        for _ in range(m):
            temp = -heapq.heappop(hq)
            
        ans += (temp*m)
    
    return ans
    
    
    