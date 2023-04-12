def solution(num, total):
    mid = total//num
    
    if num%2 == 0 :
        return [i for i in range(mid-num//2+1, mid+num//2+1)]
    else :
        return [i for i in range(mid-num//2, mid+num//2+1)]
