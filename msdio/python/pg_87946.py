from itertools import permutations

def solution(k, dungeons):
    length = len(dungeons)
    cands = list(permutations([i for i in range(length)], length))
    
    ans = 0
    for cand in cands:
        cnt = 0
        k_left = k
        
        for i in range(length):
            req, cost = dungeons[cand[i]]
            
            if k_left < req:
                continue
                
            k_left -= cost
            cnt += 1
            
        ans = max(ans, cnt)
        
    return ans