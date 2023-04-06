from itertools import combinations
import math

def is_prime(n):
    ret = True
    
    end = int(math.sqrt(n) + 1)
    for i in range(2, end):
        if(n % i == 0):
            ret = False
            break
            
    return ret

def solution(nums):
    cands = list(combinations(nums, 3))
    
    ans = 0
    for cand in cands:
        if(is_prime(sum(cand))):
            ans += 1 
            
    return ans