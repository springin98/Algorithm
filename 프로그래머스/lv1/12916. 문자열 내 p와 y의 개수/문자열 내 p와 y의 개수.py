def solution(s):
    p = [i for i in s if i=='p' or i=='P']
    y = [i for i in s if i=='y' or i=='Y']
    
    if len(p) == len(y) :
        return True
    
    else :
        return False