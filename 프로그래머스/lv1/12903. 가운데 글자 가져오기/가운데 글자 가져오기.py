def solution(s):
    s = list(s)
    # if len(s)%2 != 0:
    #     return (s[len(s)//2])
    # else :
    #     return s[len(s)//2-1]+s[len(s)//2]
    
    return (s[len(s)//2] if len(s)%2 != 0 else s[len(s)//2-1]+s[len(s)//2])