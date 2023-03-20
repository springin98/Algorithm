def solution(n):
    cnt = 0
    answer = 0
    while cnt != int(n/2) :
        cnt += 1
        answer += cnt*2
    
    return answer