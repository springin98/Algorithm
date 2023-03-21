def is_pel(str):
    if(str == str[::-1]):
        return True
    else:
        return False

    
def solution(s):
    ans = -1
    
    if(len(s) <= 1):
        return len(s)
    
    for i in range(len(s)+1):
        for j in range(i+1, len(s)+1):
            if(is_pel(s[i:j]) and j-i > ans):
                ans = j-i
    
    return ans