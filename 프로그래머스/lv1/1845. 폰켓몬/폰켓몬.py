def solution(nums):
    getNum = len(nums)/2
    nums = list(set(nums))
    
    if len(nums) >= getNum:
        return getNum
    else :
        return len(nums)