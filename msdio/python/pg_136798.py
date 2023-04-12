def cnt_divisor(number):
    if number == 1:
        return [1]
    
    arr = [1]*number
    
    for i in range(1, number // 2):
        start = i
        while start < number:
            arr[start] += 1
            start += (i+1)
            
    for i in range(number//2, number):
        arr[i] += 1
    
    return arr


def solution(number, limit, power):
    divisors = cnt_divisor(number)
    
    ans = 0
    for div in divisors:
        if div <= limit:
            ans += div
        else:
            ans += power
    
    return ans
    