def solution(array):
    array_set = list(set(array))
    answer = {}
    
    for i in array_set :
        answer[i] = array.count(i)
        
    # answer = sorted(answer.items(), key = lambda x :x[1], reverse = True)
    answer = [k for k, v in answer.items() if max(answer.values()) == v]
    
    if len(answer) > 1 :
        return -1
    else :
        return answer[0]
