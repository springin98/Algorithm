def solution(name, yearning, photo):
    dict = {}
    for i in range(len(name)):
        dict[name[i]] = yearning[i]
    
    ans = []
    
    for it in photo:
        cnt = 0
        
        for p in it:
            if(p in name):
                cnt += dict[p]
        
        ans.append(cnt)
        
    return ans
        