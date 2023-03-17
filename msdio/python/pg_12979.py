import math

def solution(n, stations, w):
    stations.sort()
    w_range = 2*w + 1
    
    ans = 0
    start = 1
    for s in stations:
        left = s - w
        right = s + w
        
        if(left <= 0):
            start = right + 1
            continue
        
        ans += math.ceil((left - start) / w_range)
        
        start = right + 1
        
    if(start <= n):
        ans += math.ceil((n - start + 1) / w_range)
    
    
    return ans
    