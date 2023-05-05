def solution(x):
    answer = sum(list(map(int, str(x))))
    
    if x%answer == 0 :
        return True
    
    else :
        return False