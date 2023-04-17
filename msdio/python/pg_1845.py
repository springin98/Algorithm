def solution(nums):
    s = set(nums)
    
    return min(len(nums)/2, len(s))