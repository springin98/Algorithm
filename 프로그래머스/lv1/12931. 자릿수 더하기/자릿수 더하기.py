def solution(n):
    list_n = list(str(n))
    answer = 0
    
    for i in list_n :
        answer += int(i)
        
    return answer