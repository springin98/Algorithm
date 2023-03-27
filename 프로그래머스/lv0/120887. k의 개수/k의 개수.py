def solution(i, j, k):
    answer = ''
    for x in range(i, j+1) :
        answer += str(x)
    answer = list(map(int, answer))
    
    return answer.count(k)