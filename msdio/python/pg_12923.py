def biggest_divisor(num):
    if num == 1:
        return 0
    
    cand = []
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            if num//i <= 10**7:
                return num // i
            
            cand.append(i)
        
    if len(cand):
        return cand[-1]
    else:
        return 1

def solution(begin, end):
    arr = [1] * (end - begin + 1)
    
    for i in range(begin, end+1):
        cal = biggest_divisor(i)
        
        arr[i - begin] = cal
        
    return arr
        
    