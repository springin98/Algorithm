def solution(array, n):
    interval = 100
    answer = 0
    
    for i in array :
        if interval > abs(i-n) :
            interval = abs(i-n)
            answer = i
        elif interval == abs(i-n) :
            if answer > i :
                answer = i
    return answer