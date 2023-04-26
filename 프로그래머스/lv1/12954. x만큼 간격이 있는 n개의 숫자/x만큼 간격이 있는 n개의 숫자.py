def solution(x, n):
    answer = []
    sum_x = 0
    
    for i in range(n) :
        sum_x += x
        answer.append(sum_x)
    
    return answer